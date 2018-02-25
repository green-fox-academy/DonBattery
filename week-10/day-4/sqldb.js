'use strict';

/* eslint linebreak-style: ['error', 'windows'] */

const mySQLdatabase = require('mysql');

module.exports = {

  initDB(username, myPassword, myDatabase) {
    return mySQLdatabase.createConnection({
      host: 'localhost',
      user: username,
      password: myPassword,
      database: myDatabase,
    });
  },

  testDB(dbCon, callback) {
    dbCon.connect((err) => {
      if (err) {
        callback(`Error connecting to database ${toString(err)}`);
      } else {
        callback('Succesfully connected to database');
      }
    });
  },

  dbError(err) {
    if (err) {
      return `Database Error ${err.toString()}`;
    }
    return 'No error';
  },

  dbQuery(dbCon, query, errorCallback, resultCallback) {
    dbCon.query(query, (err, rows) => {
      if (err) {
        errorCallback(err);
      } else {
        resultCallback(rows);
      }
    });
  },
};

