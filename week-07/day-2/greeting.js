'use strict';

// - Create variable named `al` and assign the value `Greenfox` to it
// - Create a function called `greet` that greets it's input parameter
//     - Greeting is printing e.g. `Greetings, dear Greenfox`
//     - Prepare for the special case when no parameters are given
// - Greet `al`

let al = 'GreenFox';

function greet(name){
    if (arguments.length < 1){
        return 'No Parameters'
    }
    else {
        return 'Greetings, dear ' + name
    }
}

console.log(greet(al))
console.log(greet())