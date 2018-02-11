/* eslint linebreak-style: ['error', 'windows'] */

const tools = require('./tools');

const path = require('path');

const express = require('express');

const app = express();

const PORT = 4000;


app.use(express.json());

app.use((req, res, next) => {
  tools.serverLog(req.method.concat(' ', req.url));
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

