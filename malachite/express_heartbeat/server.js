/* eslint linebreak-style: ['error', 'windows'] */

const heartbeat = require('./heartbeat');

const express = require('express');

const app = express();

const PORT = 7373;

app.use(heartbeat.endpoint);

app.get('/', (req, res) => {
  res.send('Hi');
});

app.get('/ping', (req, res) => {
  res.send('pong');
});

app.listen(PORT, () => { console.log(`test server listening on port ${PORT}`); });