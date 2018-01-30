"use strict"; // 🐸

const myURL = "http://localhost:420";

console.log("page loaded");

displayMessage("Search by Licence plate pattern ABC-123 or fragment of pattern", false);

let searchButton = document.getElementById("searchButton");
let resetButton = document.getElementById("resetButton");
let searchForm = document.getElementById("searchForm");

searchButton.addEventListener("click", searchDB);

searchButton.addEventListener("click", resetForm);

function displayMessage(text, error = false) {
  let messageBox = document.getElementById('message');
  error ? messageBox.classList = "errorMessage" : messageBox.classList = "normalMessage";
  messageBox.innerHTML = text;  
}

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

function resetForm() {
  searchForm.reset();
  resetResultBox();
  displayMessage("Search by Licence plate pattern ABC-123 or fragment of pattern", false);  
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
  let messageBox = document.getElementById('message');
  if (rows.hasOwnProperty("Error")) {
    displayMessage("Wrong query", true);
  } else if (rows.length === 0) {
    displayMessage("No match for your query", false);
  } else {
    resetResultBox();
    rows.forEach(row => {renderRow(row)});
  }
}

function getChecked(radios) { 
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) {
      return radios[i].value;
    }
  }
  return "";
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
  // console.log(`\nGeneral request sent with method: ${method} \nURL: ${URL} \nquery: ${query} \nparameters: ${parameters} \nfragment: ${fragment} \nheader: ${header} \nbody: ${body}`);
  let MyRequester = new XMLHttpRequest();
  MyRequester.open(method, URL);
  if (header === "JSON") {
    MyRequester.setRequestHeader("Content-Type", "application/json");
    MyRequester.setRequestHeader("Accept", "application/json");
  }
  MyRequester.send(JSON.stringify(body));  
  MyRequester.onload = function () {onloadFunction(JSON.parse(MyRequester.responseText))};
}