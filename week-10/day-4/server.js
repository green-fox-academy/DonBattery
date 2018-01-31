"use strict"; // 🐸

const PORT = 3000;
const mySQL = require("mysql");
const Express = require("express");
const app = Express();
const dbCon = initDB();

function connectDatabase () {
  dbCon.connect((err) => {
    if(err){
      console.log(`Error connecting to database ${toString(err)}`);
      return;
    }
    console.log("Succesfully connected to database");
  });
}

function initDB() {
  let conn = mySQL.createConnection({
    host: "localhost",
    user: "root",
    password: "pass123",
    database: "cars"
  });
  return conn;
}

function dbError (err, res) {
  if(err) {
    console.log(`Database Error ${err.toString()}`);
    res.status(500).send("Database Error");
  }
}

app.use(Express.json());

app.use(function (req, res, next) {
  console.log(req.method + " " + req.url);
  next();
});

app.use(Express.static("page"));

app.get("/*", (req, res) => {
  res.status(404);
  res.json(`Wrong way! 🐸`);  
});

connectDatabase();

app.listen(PORT, () => {console.log(`\nTable Server listening on PORT : ${PORT}\n`)});