'use strict';

/* eslint linebreak-style: ["error", "windows"] */

const PORT = 8080;

const Express = require('express');

const app = Express();

app.use(Express.json());

app.use((req, res, next) => {
  console.log(req.method + " " + req.url);
  next();
});

app.use(Express.static('page'));

app.get('/:id/:name', (req, res, next) => {
  console.log('Query :', req.query);
  console.log('Params :', req.params);
  next();
});

app.get('/*', (req, res) => {
  console.log('Query :', req.query);
  console.log('Params :', req.params);
  res.status(200).send('Jó');
});

app.listen(PORT, () => { console.log(`\nPager Server listening on PORT : ${PORT}`); });
