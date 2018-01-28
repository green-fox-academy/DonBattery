"use strict"; // 🐸

//  . o O Tiny JavaScript Server running on Node.js Nodemon O o .

// Express will be our web-framework 
const express = require('express');

// Dunno if this needed anymore ??? express also can parse JSON
const bodyParser = require('body-parser');

// Miki tools 
const Tools = require('./tools.js');

// This is the PORT Tyiny JS Server will listen to, so localhost:PORT will be the / (root) on our computer. 
// Other clients on the network can reach the same root as <this computer's IP:PORT> 192.168.0.17:6969 for example
const PORT = 6969

// Summon the Express framework
const app = express();

// wat u do ?
let urlPraser = bodyParser.urlencoded({ extended: false });

// This function writes the server log onto the terminal where the server was summoned by Nodemon (actually this should go into a file...)
function logIP(reqIP, message = "general") {
  console.log(`${message} request on: ${Tools.formatDate()} from IP: ${Tools.getIPaddress(reqIP)}`);
}

// And this is where things geting wierd...

// This parses the request so we can refer to its properties as JS Objest properties
app.use(express.json());

// This needs to determine incoming IP adresses (the "trust" keyword indicates this may be not the best solution regarding security)
app.enable('trust proxy');


// First midleware will log the request info onto the terminal (this needs to be extended with more data, and appended into a log-file)
app.use(function (req, res, next) {
    logIP(req.ip, req.method + " " + req.url);
    next();
  });

// Root endpoint. Load mainpage from BaseURL / -> index.html 
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/page/index.html');
});

// As we do not host static library (jet) we need each file relating to frontend hosted individually
// Load ffavicon
app.get('/favicon.ico', (req, res) => {
  res.sendFile(__dirname + '/page/favicon.ico');
});

// Load mainpage stylesheet
app.get('/style.css', (req, res) => {
  res.sendFile(__dirname + '/page/style.css');
});

// Load page JS code
app.get('/page.js', (req, res) => {
  res.sendFile(__dirname + '/page/page.js');
});

// Experimental part testing Login roght now
app.post('/login', urlPraser, function (req, res) {
  console.log('Base URL :', req.baseUrl);
  console.log('Request Body :', req.body);
  if (!'username' in req.body) {
    return res.status(400).send("username missing");
  } else {
    res.send('welcome, ' + req.body.username);
  }
});

// All other (incorrect) request will fall to this pit resulting a 404 error (maybe a funny picture ?)
app.get('/*', (req, res) => {
  res.status(404);
  res.json(`Wrong way! 🐸`);  
});

// This aweakens the Express so it begins its work: listen on the PORT -> catch requests -> make it flow through the middlewares, rooters arriving to endpoints
// meanwhile performing various matgic 💥 
app.listen(PORT, function(){console.log(`\nTiny JS server listening on PORT : ${PORT}\n`)});
