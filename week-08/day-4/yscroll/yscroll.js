"use strict";

let testObj = {
    "key" : "value"
} 

function post(postObj, i) {
    let textElement = document.createElement('div');
    textElement.innerHTML = postObj["key"]
    textElement.id = "post" + i
    let testElement = document.createElement('div');
    testElement.innerHTML = "test"
    document.getElementById('test').appendChild(textElement);
    document.getElementById('post' + i).appendChild(testElement);
}

for (let i = 0; i < 100; i++){
    post({"key" : "csigahányás"}, i)
}