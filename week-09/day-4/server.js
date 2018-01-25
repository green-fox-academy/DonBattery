"use strict";

const express = require('express');
const bodyParser = require('body-parser');

const PORT = 6969

const app = express();

let logged = false;

app.use(bodyParser.json());

app.enable('trust proxy');

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function formatDate() {
  
  let date = new Date();

  let day = date.getDate();
  let month = date.getMonth() + 1;
  let year = date.getFullYear();
  let hour = date.getHours();
  let min = date.getMinutes();
  let sec = date.getSeconds();

  return `${year}.${month}.${day} at: ${hour}:${min}:${sec}`;
}

function getIPaddress(inputString) {
  if (typeof inputString != "string") {
    return -1;
  } else {
    let temp = "";
    let i = 0;
    let foundStart = false;
    while (i < inputString.length) {
      if (isNumeric(inputString[i]) || foundStart) {
        foundStart = true;
        temp += inputString[i]
      }
      i++;
    }
    if (temp === "1" || temp === "127.0.0.1") {
      return "localhost"
    } else {
      return temp;
    }
  }
}

function logIP(reqIP, message = "general") {
  logged = true;
  console.log(`${message} request on: ${formatDate()} from IP: ${getIPaddress(reqIP)}`);
}

function double(value) {
  if (value === undefined) {
    return {"error" : "Please provide an input!"}
  } else {
    return {"received": value, "result": value * 2};
  }  
}

function greeter(name, title) {
  if (name === undefined) {
    return {"error": "Please provide a name!"}
  } else if (title === undefined) {
    return {"error": "Please provide a title!"}
  } else {
    return {"welcome_message" : `Oh, hi there ${name}, my dear ${title}!`}
  }  
}

function appenda(params) {
  return {"appended" : params + "a"}  
}

app.use('/assets', express.static('assets'));

app.get('/', (req, res) => {
  logIP(req.ip, "page load");
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', (req, res) => {
  logIP(req.ip, "doubling");
  res.json(double(req.query["input"]))
})

app.get('/greeter', (req, res) => {
  logIP(req.ip, "greeter");
  res.json(greeter(req.query["name"], req.query["title"]))
}); 

app.get('/appenda/*', (req, res) => {
  logIP(req.ip, "appenda");
  res.json(appenda(req.params[0]));
}); 

app.get('/*', (req, res) => {
  if (!logged) {
    logIP(req.ip);
    logged = false;
  }
  res.status(404);
  res.json("wrong way!")  
});

app.listen(PORT, function(){console.log(`\nTiny JS server listening on PORT : ${PORT}\n`)});