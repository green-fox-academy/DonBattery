"use strict"; // 🐸

//  . o O Tiny JavaScript Server running on Node.js Nodemon O o .

// MySQL is our database 
const mysql = require("mysql");

// Express will be our web-framework 
const express = require("express");

// Dunno if this needed anymore ??? express also can parse JSON
const bodyParser = require("body-parser");

// Miki tools 
const Tools = require("./tools.js");

// This is the PORT Tyiny JS Server will listen to, so localhost:PORT will be the / (root) on our computer. 
// Other clients on the network can reach the same root as <this computer's IP:PORT> 192.168.0.17:6969 for example
const PORT = 6969

// Summon the Express framework
const app = express();

// wat u do ?
let urlPraser = bodyParser.urlencoded({ extended: false });

// SQL things ahead (these may go to a separate file)
// this variable represents our connection to the database
let dbCon = initDB();

// Test the connection to the database and log result
function connectDatabase () {
  dbCon.connect((err) => {
    if(err){
      serverLog(`Error connecting to database ${toString(err)}`);
      return;
    }
    serverLog("Succesfully connected to database");
  });
};

// Init the tatabase to linkchat and return the connection object
function initDB() {
  let conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "pass123",
    database: "linkchat"
  });
  return conn
};

// callback function for later error-log and apropirate response to client
function dbError (err, res) {
  if(err) {
    serverLog(`Database Error ${err.toString()}`);
    res.status(500).send("Database Error");
  }
};
// end of SQL things

// This function writes the server log onto the terminal where the server was summoned by Nodemon (actually this should go into a file...)
function serverLog(message) {
  console.log(`Time : ${Tools.formatDate()} ${message}`);
}

// General request logger with IP
function logIP(reqIP, message = "general") {
  serverLog(`${message} request from IP: ${Tools.getIPaddress(reqIP)}`);
}

// Aaand this is where things geting wierd...

// This parses the request so we can refer to its properties as JS Objest properties
app.use(express.json());

// This needs to determine incoming IP adresses (the "trust" keyword indicates this may be not the best solution regarding security)
app.enable("trust proxy");

// First midleware will log the request info onto the terminal (this needs to be extended with more data, and appended into a log-file)
app.use(function (req, res, next) {
  logIP(req.ip, req.method + " " + req.url);
  next();
});

// experimental static host of page directory as root
app.use(express.static("page"))

// return the posts from database ordered by points
app.get("/posts", (req, res) => {
  dbCon.query('SELECT * FROM posts ORDER BY points DESC;', (err, rows) => { err ? dbError(err, res) : res.json({'posts': rows})});
});

// return the users from database minus the passwords
app.get("/users", (req, res) => {
  dbCon.query('SELECT USER_ID, username, profile_pic FROM users;', (err, rows) => { err ? dbError(err, res) : res.json({'users': rows})});
});

// Experimental part testing Login roght now
app.post("/login", urlPraser, function (req, res) {
  console.log("Base URL :", req.baseUrl);
  console.log("Request Body :", req.body);
  if (!"username" in req.body) {
    return res.status(400).send("username missing");
  } else {
    res.send("welcome, " + req.body.username);
  }
});

// All other (incorrect) request will fall to this pit resulting a 404 error (maybe a funny picture ?)
app.get("/*", (req, res) => {
  res.status(404);
  res.json(`Wrong way! 🐸`);  
});

// Finally init our things, and run the server!
// Lets init our database
connectDatabase();
// This aweakens the Express so it begins its work: listen on the PORT -> catch requests -> make it flow through the middlewares, rooters arriving to endpoints
// meanwhile performing various matgic 💥 
app.listen(PORT, function(){console.log(`\nTiny JS server listening on PORT : ${PORT}\n`)});
