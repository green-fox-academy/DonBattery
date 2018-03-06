'use strict';

const myUrl = 'http://localhost:801';

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
          readyCallback(myRequest.responseText);
          break;
        default:
          errorCallback(`Status : ${myRequest.status} Text : ${myRequest.statusText}`);
      }
    }
  };
  myRequest.send(body);
}

function onLoadLogger(params) {
  console.log('Loaded :', params);    
}

function onErrorLogger(params) {
  console.log('Error :', params);    
}

function onPageLod() {
  myRequester('GET', 'text', myUrl, ['jiff'], {}, null, onLoadLogger, onErrorLogger);
}

window.addEventListener('load', onPageLod);