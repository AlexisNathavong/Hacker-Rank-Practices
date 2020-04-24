'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the breakingRecords function below.
function breakingRecords(scores) {
    // set a highScore to 0 as it's starting point and set lowScore to 0 as it's starting point aswell
    let [highScore, lowScore] = [0, 0];
    let [newHighScore, newLowScore] = [scores[0], scores[0]];

    // for loop to loop through the scores array to find how many times Maria breaks her highest score and lowest score
    for (let i = 1; i < scores.length; i++) {
        // highest score
        if (scores[i] > newHighScore) {
            // resest the newHighScore as the newest highest score
            newHighScore = scores[i];
            // add how many times Maria breaks her highest score
            highScore++;
        }
        
        // lowest score
        if (scores[i] < newLowScore) {
            // resest the newLowScore as the newest lowest score
            newLowScore = scores[i];
            // add how many times Maria breaks her lowest score
            lowScore++;
        }
    }

    // print the high score and low score counts
    return [highScore, lowScore];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const scores = readLine().split(' ').map(scoresTemp => parseInt(scoresTemp, 10));

    const result = breakingRecords(scores);

    ws.write(result.join(' ') + '\n');

    ws.end();
}
