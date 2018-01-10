'use strict';

// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(til){
    let value = 0
    for (let i = 1; i < til; i++){
        value = value + i
    }
    return value
}

console.log(sum(1))

console.log(sum(100))