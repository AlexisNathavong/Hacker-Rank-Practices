'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the plusMinus function below.
function plusMinus(arr) {
    // set the counters for positive, negative, and zero
    let posCount = 0;
    let negCount = 0;
    let zerCount = 0;

    // for each integer in the array, increment the counters depending on the form of the integer
    arr.forEach( i => {
        if (i > 0) { 
            posCount++;
        }
        else if (i < 0) {
            negCount++;
        }
        else {
            zerCount++;
        }
    })
    
    // create the fractions from the counts and convert to decimals
    console.log((posCount/ arr.length).toFixed(6));
    console.log((negCount/ arr.length).toFixed(6));
    console.log((zerCount/ arr.length).toFixed(6));

}

function main() {
    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
