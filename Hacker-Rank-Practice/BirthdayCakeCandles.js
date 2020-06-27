'use strict';

const fs = require('fs');

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

// Complete the birthdayCakeCandles function below.
function birthdayCakeCandles(ar) {
// It must return an integer representing the number of candles she can blow out.


let maxCandles = 0;
let count = 0;
// For loop - loop through to see how many candles can be blown out by my niece.
for (let i = 0; i < ar.length; i++) {
    if (ar[i] > maxCandles) {
        maxCandles = ar[i];
        count = 1;

    } else if (ar[i] === maxCandles) {
        count++;
     }
        
    }
return(count);
}



function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const arCount = parseInt(readLine(), 10);

    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));

    let result = birthdayCakeCandles(ar);

    ws.write(result + "\n");

    ws.end();
}
