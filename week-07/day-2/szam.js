'use strict';

// Create a simple calculator application which does read the parameters from the standard input 
// and prints the result to the console.

// It should support the following operations: 
// +, -, *, /, % and it should support two operands. 

// The format of the expressions must be: {operation} {operand} {operand}. 
// Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

// You should use the command line arguments to accept user input

// It should work like this:

// Start the program with "node calculator.js + 5 6"
// If number of arguments are not correct, print some nice errors
// Else print the result
// Say goodbye

let args = process.argv.splice(2); // Just a helper for you to get started

let validOperations = ['+', '-', '*', '/']

function usage(){
    console.log('\nCalculator')
    console.log('Usage : node szam.js {operation} {operand} {operand}')
    console.log('Operation can be + - * or / Operand can be an integer or a float')
    process.exit()
}

if (args.length != 3){
    console.error('Not enugh arguments')
    usage()
}
else {
    if (validOperations.indexOf(args[0]) === -1){
        console.error(args[0] + ' is not a valid operator')
        usage()
    }
    if ((isNaN(args[1])) || (isNaN(args[2]))){
        console.log(isNaN(args[1]))
        console.error('Please enter numbers as operands')
        usage()
    }
    let a = Number(args[1])
    let b = Number(args[2])
    
    if (args[0] === '+'){
        console.log(a + b)
    }   
    if (args[0] === '-'){
        console.log(a - b)
    }   
    if (args[0] === '*'){
        console.log(a * b)
    }   
    if (args[0] === '/'){
        console.log(a / b)
    }   
}
