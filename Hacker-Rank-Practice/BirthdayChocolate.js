'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the birthday function below.
function birthday(s, d, m) {
// Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m =2.

// You must determine how many ways she can divide the chocolate.

// resultCount - returns the number of ways Lily can divide the chocolate bar.
let resultCount = 0;

// reducer - to add up the sum and return the sum.
let reducer = (a,b) => (a + b);

// Loop through the array to determine how many ways the bar can be split.
for (let i = 0; i < s.length; i++) {
    if (s.slice(i, i+m).reduce(reducer) == d) {
        resultCount++
    }
}

// It should return an integer denoting the number of ways Lily can divide the chocolate bar.
return resultCount;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const s = readLine().replace(/\s+$/g, '').split(' ').map(sTemp => parseInt(sTemp, 10));

    const dm = readLine().replace(/\s+$/g, '').split(' ');

    const d = parseInt(dm[0], 10);

    const m = parseInt(dm[1], 10);

    const result = birthday(s, d, m);

    ws.write(result + '\n');

    ws.end();
}
