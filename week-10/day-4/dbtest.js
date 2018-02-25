'use strict';

/* eslint linebreak-style: ["error", "windows"] */

const db = require('./sqldb.js');

const mySQL = db.initDB('root', 'pass123', 'cars');

function logger(message) {
  console.log(message);
  console.log('\nROW', message[0], '\n');
  console.log(typeof message[0]);
  console.log(message[1].plate);
  console.log(JSON.stringify(message));
}

function logger2(message) {
  console.log(message.toString());
}

db.testDB(mySQL, logger);

db.dbQuery(mySQL, `SELECT * FROM licence_plates WHERE plate like 'R%';`, logger2, logger);

console.log('ended');
