'use strict';

/* eslint linebreak-style: ['error', 'windows'] */

const PORT = 6969;

const Express = require('express');

const mysql = require('mysql');

const app = Express();

const dbCon = initDB();

function serverLog(message) {
  const date = new Date();
  const hour = date.getHours();
  const min = date.getMinutes();
  const sec = date.getSeconds();
  console.log(`${hour}:${min}:${sec} - ${message}`);
}

function initDB() {
  const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'pass123',
    database: 'sajt',
  });
  return conn;
}

function askDB(query, onLoad = () => {}, onError = () => {}) {
  dbCon.query(query, (err, rows) => {
    if (err) { onError(err); } else { onLoad(rows); }
  });
}

app.use(Express.json());

app.use((req, res, next) => {
  serverLog(req.method.concat(' ', req.url));
  next();
});

app.use(Express.static('page'));

app.get('/planets', (req, res) => {
  askDB('SELECT * FROM planet', (rows) => { res.status(200).json({ planets: rows }); });
});

app.get('/ship', (req, res) => {
  askDB('SELECT * FROM spaceship', (rows) => { res.status(200).json({ ship: rows }); });
});

function getPlanetIDByName(planetName, planets) {
  let id = -1;
  planets.forEach((planet) => {
    if (planetName === planet.name) { id = planet.id; }
  });
  return id;
}

app.post('/movehere/:planetId', (req, res) => {
  askDB('SELECT id, name FROM planet', (planetData) => {
    askDB('SELECT planet FROM spaceship WHERE ID = 1', (shipData) => {
      const shipPosition = getPlanetIDByName(shipData[0].planet, planetData);
      if ((planetData.some(planet => (planet.id == req.params.planetId))) && ((req.params.planetId !== shipPosition))) {
        askDB(`UPDATE spaceship SET planet = '${planetData[req.params.planetId - 1].name}' WHERE id = 1`, () => {
          res.status(200).send({ Succes: 'Moved' });
        }, () => {
          res.status(500).json({ Error: 'DatabaseError 1' });
        });
      }
    }, () => { res.status(500).json({ Error: 'DatabaseError 2' }); });
  }, () => { res.status(500).json({ Error: 'DatabaseError 3' }); });
});

app.post('/toplanet', (req, res) => {
  askDB('SELECT * FROM spaceship WHERE id = 1', (shipData) => {
    askDB(`UPDATE planet SET population = population + ${shipData[0].utilization} WHERE name = '${shipData[0].planet}'`, () => {
      askDB('UPDATE spaceship SET utilization = 0 WHERE id = 1', () => {
        res.status(200).json({ Succes: 'ToPlanet' });
      }, () => { res.status(500).json({ Error: 'DatabaseError 1' }); });
    }, () => { res.status(500).json({ Error: 'DatabaseError 2' }); });
  }, () => { res.status(500).json({ Error: 'DatabaseError 3' }); });
});

app.post('/toship', (req, res) => {
  askDB('SELECT * FROM spaceship WHERE id = 1', (shipData) => {
    askDB('SELECT * FROM planet', (planetData) => {
      let population = planetData[getPlanetIDByName(shipData[0].planet, planetData) - 1].population;
      let utilization = shipData[0].utilization;
      const freeSpace = shipData[0].max_capacity - shipData[0].utilization;
      if (population <= freeSpace) { utilization += population; population = 0; } else {
        population -= freeSpace; utilization = shipData[0].max_capacity;
      }
      askDB(`UPDATE planet SET population = ${population} WHERE name = '${shipData[0].planet}'`, () => {
        askDB(`UPDATE spaceship SET utilization = ${utilization} WHERE id = 1`, () => {
          res.status(200).json({ Succes: 'ToShip' });
        }, () => { res.status(500).json({ Error: 'DatabaseError 1' }); });
      }, () => { res.status(500).json({ Error: 'DatabaseError 2' }); });
    }, () => { res.status(500).json({ Error: 'DatabaseError 3' }); });
  }, () => { res.status(500).json({ Error: 'DatabaseError 4' }); });
});

app.get('/*', (req, res) => {
  res.status(404).send('Wrong way... 🐸');
});

app.listen(PORT, () => { serverLog(`SPACERACE Server listening on PORT : ${PORT}`); });
