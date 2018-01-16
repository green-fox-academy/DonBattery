'use strict';

function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

function rnd_string(a, b, end){
    let diff = Math.abs(a - b);
    let off = 0;
    (a > b) ? off = b : off = a;
    return (Math.floor((Math.random() * diff) + off)).toString() + end
}

function addButton(){
    let btn = document.createElement("BUTTON");        // Create a <button> element

    btn.style.height = rnd_string(30, 350, 'px');
    btn.style.width = rnd_string(40, 180, 'px');

    //btn.style.height = (Math.floor((Math.random() * 170) + 30)).toString() + 'px';
    //btn.style.height = (Math.floor((Math.random() * 170) + 30)).toString() + 'px';

    btn.style.fontSize = rnd_string(8, 64, 'px');

    let t = document.createTextNode("⌨");       // Create a text node

    btn.appendChild(t);                                // Append the text to <button>
    document.body.appendChild(btn);                    // Append <button> to <body>
}

function addRandomBox(){

    let box = document.createElement('div');

    box.style.height = '30px'
    box.style.width = rnd_string(20,60, 'px');
    box.style.display = 'inline-flex'
    box.style.lineHeight = '10%'
    box.style.backgroundColor = getRandomColor();

    document.body.appendChild(box);
}

document.body.style.height = '100%';
document.body.style.width = '100%';

for (let i = 0; i < 100; i++){
    //addButton();
    //addRandomBox();
}