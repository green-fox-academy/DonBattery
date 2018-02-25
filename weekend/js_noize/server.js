/* eslint linebreak-style: ['error', 'windows'] */

const tools = require('./tools');

const path = require('path');

const mySQL = require('mysql');

const express = require('express');

const db = tools.initDB(mySQL, 'localhost', 'root', 'pass123', 'js_noize');

const app = express();

const PORT = 4001;

// TEST LINE
tools.askDB(db, 'SELECT * FROM tet', (rows) => { console.log('query :', rows); }, (err) => { console.log('db error :', err.toString()); });

app.enable('trust proxy');

app.use(express.json());

app.use((req, res, next) => {
  tools.serverLog(req.method.concat(' request from ', tools.getIPaddress(req.ip), ' ', req.url));
  next();
});

app.use(express.static(path.join(__dirname, 'page')));

app.use((req, res) => {
  res.status(404).send('Wrong way... 🐸');
});

app.use((err, req, res) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong... 🐸');
});

app.listen(PORT, () => { tools.serverLog('Test Server listening on PORT :'.concat(PORT.toString())); });

