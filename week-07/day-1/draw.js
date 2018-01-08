'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for (let i = 1; i <= lineCount; i++){
    let sim = '#'.repeat(i)
    console.log(sim)
}

var lineCount = 4;

for (let i = 0; i < lineCount; i++){
    let sim = ' '.repeat(lineCount - i - 1) + '#'.repeat(i * 2 + 1)
    console.log(sim)
}

console.log('________________________________________________')
console.log('The grate diamond drawing machine')
console.log('________________________________________________\n')

var lineCount = 7;

let paros = lineCount % 2 == 0

if (paros == true) {
    let middle = lineCount / 2
    for (let i = 0; i < middle; i++){
        let sim = ' '.repeat(middle - i - 1) + '#'.repeat(i * 2 + 2)
        console.log(sim)
    }
    for (let i = middle; i > 0; i--){
        let sim = ' '.repeat(middle - i) + '#'.repeat(i * 2)
        console.log(sim)
    }
}
else {
    let middle = lineCount - 1 / 2
    for (let i = 0; i < middle; i++){
        let sim = ' '.repeat(middle - i) + '#'.repeat(i * 2 + 1)
        console.log(sim)
    }
    for (let i = middle - 1; i > 0; i--){
        let sim = ' '.repeat(middle - i) + '#'.repeat(i * 2)
        console.log(sim)
    }
}
