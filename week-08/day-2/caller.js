
'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

function selectLastEvenNumber(myArr, call) {
    let lasteven = -1;
    for (let i = 0; i < myArr.length; i++) {
        if (myArr[i] % 2 === 0) {
            lasteven = myArr[i]
        }
    }
    if (lasteven != -1) {
        call(lasteven)
    }
}

function printNumber(num) {
  console.log(num);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8