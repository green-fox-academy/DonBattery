"use strict"; // 🐸

const myURL = "http://localhost:420";

console.log("page loaded");

let searchButton = document.getElementById("searchButton");

searchButton.addEventListener("click", searchDB);

function resetResultBox() {
  let resultBox = document.getElementById('resultBox');
  resultBox.innerHTML = `
    <tr>
      <th>Plate</th>
      <th>Brand</th> 
      <th>Model</th>
      <th>Color</th>
      <th>Year</th>
    </tr>`;
}

function getChecked(radios) { 
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) {
      return radios[i].value;
    }
  }
  return -1;
}

function renderRow(row) {
  let resultBox = document.getElementById('resultBox');
  resultBox.innerHTML += `
  <tr>
    <td>${row.plate}</td>
    <td>${row.car_brand}</td> 
    <td name = "carModel">${row.car_model}</td>
    <td>${row.color}</td>
    <td>${row.year}</td>
  </tr>
  `;
}

function renderResult(rows) {
  console.log(rows);
  resetResultBox();
  rows.forEach(row => {renderRow(row)});
}

function searchDB() {
  let inputText = document.getElementById('inputText');
  let radios = document.getElementsByName('licenceType');
  let checkedRadio = getChecked(radios);
  generalRequest("GET", myURL + "/search", {"inputText" : inputText.value, "licenceType" : checkedRadio}, {}, {}, "JSON", {}, renderResult);
}

function generalRequest(method = "GET", URL = rootURL, query = {}, parameters = {}, fragment = {}, header = {}, body = {}, onloadFunction = function () {}) {
  if (Object.keys(query).length != 0) {
    URL += `?${Object.keys(query).map(key => key + '=' + encodeURIComponent(query[key])).join('&')}`;
  }
  console.log(`\nGeneral request sent with method: ${method} \nURL: ${URL} \nquery: ${query} \nparameters: ${parameters} \nfragment: ${fragment} \nheader: ${header} \nbody: ${body}`);
  let MyRequester = new XMLHttpRequest();
  MyRequester.open(method, URL);
  if (header === "JSON") {
    MyRequester.setRequestHeader("Content-Type", "application/json");
    MyRequester.setRequestHeader("Accept", "application/json");
  }
  MyRequester.send(JSON.stringify(body));  
  MyRequester.onload = function () {onloadFunction(JSON.parse(MyRequester.responseText))};
}




