'uses strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

let allsec = 24 * 60 * 60
let remainingsec = allsec - currentHours * 60 * 60 + currentMinutes * 60 + currentSeconds

console.log(remainingsec + ' scound is remaining from this Day')