"use strict"; // 🐸

//  . o O Node Noise Music Server O o .

const mysql = require("mysql");
const express = require("express");
const Tools = require("./tools.js");

const PORT = 3000

const app = express();
const dbCon = initDB();

function connectDatabase () {
  dbCon.connect((err) => {
    if(err){
      serverLog(`Error connecting to database ${toString(err)}`);
      return;
    }
    serverLog("Succesfully connected to database");
  });
};

function initDB() {
  let conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "pass123",
    database: "noise"
  });
  return conn
};

function dbError (err, res) {
  if(err) {
    serverLog(`Database Error ${err.toString()}`);
    res.status(500).send("Database Error");
  }
};

function serverLog(message) {
  console.log(`Time : ${Tools.formatDate()} ${message}`);
}

function logIP(reqIP, message = "general") {
  serverLog(`${message} request from IP: ${Tools.getIPaddress(reqIP)}`);
}

app.use(express.json());

app.enable("trust proxy");

app.use(function (req, res, next) {
  logIP(req.ip, req.method + " " + req.url);
  next();
});

app.use(express.static("page"))

app.get("/*", (req, res) => {
  res.status(404);
  res.json(`Wrong way! 🐸`);  
});

connectDatabase();

app.listen(PORT, function(){console.log(`\nNode Music Server listening on PORT : ${PORT}\n`)});