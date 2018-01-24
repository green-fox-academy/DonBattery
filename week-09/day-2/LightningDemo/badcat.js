"use strict";

let boxClasses = ["box1", "box2", "box3", "box4", "box5"];
let boxTexts = ["Wut", "Python Rulez", "Yo", "Hello", "BadCat"];

function randint(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function createMoar() {
  let buddy = document.getElementById("building");
  let newBox = document.createElement('div');
  newBox.classList = boxClasses[randint(0, 4)];
  newBox.innerHTML = boxTexts[randint(0, 4)];
  newBox.style.display = "inline-block";
  buddy.appendChild(newBox);
}

document.getElementById("BUTTON").onclick = createMoar;