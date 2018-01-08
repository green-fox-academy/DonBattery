'use strict';

var favoriteNumber = 8
// Store your favorite number in a variable (as a number)
// And print it like this: 'My favorite number is: 8'
console.log('My favorite number is :' + favoriteNumber + '\n')

// Swap the values of these variables
var a = 123;
var b = 526;
console.log('Before swap')
console.log('a :'+ a);
console.log('b :'+ b + '\n');

var c = a;
a = b;
b = c;

console.log('After swap')
console.log('a :'+ a);
console.log('b :'+ b + '\n');

var massInKg = 81.2;
var heightInM = 1.78;

// Print the Body mass index (BMI) based on these values

console.log('massInKg = 81.2')
console.log('heightInM = 1.78')
console.log('BMI :' + massInKg / Math.pow(heightInM, 2) + '\n')

var a = 3;
// make it bigger by 10

a = a + 10;

console.log(a);




var b = 100;
// make it smaller by 7
b = b - 7;

console.log(b);




var c = 44;
// double c's value
c = c * 2;

console.log(c);




var d = 125;
// divide d's value by 5
d = d / 5;

console.log(d);




var e = 8;
// what's the cube of e's value?
Math.pow(e, 2)

console.log(e);




var f1 = 123;
var f2 = 345;
// tell if f1 is bigger than f2 (as a boolean)

if (f1 > f2){
    console.log('True')
}
else{
    console.log('False')
}


var g1 = 350;
var g2 = 200;
// tell if the double of g2 is bigger than g1 (pras a boolean)




var h = 1357988018575474;
// tell if h has 11 as a divisor (as a boolean)
if (h % 11 == 0){
    console.log(h + ' has 11 as a divisor')
    console.log(h + ' / 11 is ' + h / 11)
}
else {
    console.log(h +  ' has not 11 as a divisor')
}



var i1 = 10;
var i2 = 3;
// tell if i1 is higher than i2 squared and smaller than i2 cubed (as a boolean)




var j = 1521;
// tell if j is dividable by 3 or 5 (as a boolean)




var k = 'Apple';
// fill the k variable with its content 4 times
k = k.repeat(4)

console.log(k);

