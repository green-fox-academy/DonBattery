'use strict';

/* eslint linebreak-style: ['error', 'windows'] */

const myUrl = 'http://localhost:6969';

function myRequester(method = 'GET', type = 'text', url = '', parameters = [], querys = {}, body = null, readyCallback = () => {}, errorCallback = () => {}) {
  const reqURL = url.concat('/', parameters.join('/'), (querys.length > 0) ? '?'.concat(Object.keys(querys).map(key => key.concat('=', encodeURIComponent(querys[key]))).join('&')) : '');
  const myRequest = new XMLHttpRequest();
  myRequest.open(method, reqURL);
  if (type === 'JSON') {
    myRequest.setRequestHeader('Content-Type', 'application/json');
    myRequest.setRequestHeader('Accept', 'application/json');
  }
  myRequest.onreadystatechange = function myLoader() {
    if (myRequest.readyState === 4) {
      switch (myRequest.status) {
        case 200:
          readyCallback(JSON.parse(myRequest.responseText));
          break;
        default:
          errorCallback(`Status : ${myRequest.status} Text : ${myRequest.statusText}`);
      }
    }
  };
  myRequest.send(body);
}

function renderRow(target, row, shipData) {
  target.innerHTML += `<td>${row.name}</td><td>${row.population}</td>
  ${(row.name === shipData[0].planet) ? (`<td><button class="button" id="toplanet">🌑TO PLANET</button><button class="button" id="toship">TO SHIP🚀</button></td><td>${shipData[0].utilization}</td>`)
    : (`<td><button class="button" id="movehere/${row.id}">MOVE HERE</button></td>`)}`;
}

function render(planetData, shipData) {
  const mainTable = document.getElementById('myTable');
  mainTable.innerHTML = '';
  planetData.forEach((row) => { renderRow(mainTable, row, shipData); });
}

function loadTable() {
  myRequester('GET', 'JSON', myUrl, ['ship'], {}, null, (shipData) => {
    myRequester('GET', 'JSON', myUrl, ['planets'], {}, null, (planetData) => {
      render(planetData.planets, shipData.ship);
      [...document.getElementsByClassName('button')].forEach((button) => {
        button.addEventListener('click', () => { myRequester('POST', 'JSON', myUrl, [button.id], {}, null, loadTable); });
      });
    });
  });
}

window.addEventListener('load', loadTable);

