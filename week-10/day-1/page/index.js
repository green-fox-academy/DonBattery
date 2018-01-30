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

function searchDB(query) {
  let inputText = document.getElementById('inputText');
  let radios = document.getElementsByName('licenceType');
  let checkedRadio = getChecked(radios);
  console.log(checkedRadio);

    //  THIS NEED TO BE EXTENDED 
  // generalRequest("GET", myURL + "/search", {}, {}, {}, "JSON", {}, (parsed) => {users = parsed.users}); 
}

function generalRequest(method = "GET", URL = rootURL, query = {}, parameters = {}, fragment = {}, header = {}, body = {}, onloadFunction = function () {}) {
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




