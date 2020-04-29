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

// Complete the compareTriplets function below.
function compareTriplets(a, b) {
    // Set Alice's score and Bob's score to both zero as a starting point.
    let [aliceScore, bobScore] = [0, 0];
    

    // Loop through the array of a to compare Alice's score to Bob's score.
    for (let i = 0; i < a.length; i++) {
        // if Alice's score is greater than Bob's score, then Alice gets a point.
        if (a[i] > b[i]) {
            aliceScore++;

        // if Alice's score is less than Bob's score, then Bob gets a point.
        } else if (a[i] < b[i]) {
            bobScore++;
        }
    }
    // Return Alice's score first then Bob's.
    return[aliceScore, bobScore];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    const b = readLine().replace(/\s+$/g, '').split(' ').map(bTemp => parseInt(bTemp, 10));

    const result = compareTriplets(a, b);

    ws.write(result.join(' ') + '\n');

    ws.end();
}
