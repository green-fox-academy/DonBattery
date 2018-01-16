"use strict";

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

function getEs(sString){
    let count = 0;
    for (let i = 0; i < sString.length; i++) {
        if (sString[i] === 'e') {
            count++;
        }
    }
    return count;
}    

let countEs = fruits.map(getEs)

console.log(fruits)
console.log(countEs)

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.