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

// Complete the hurdleRace function below.
function hurdleRace(k, height) {
    // Set minDoses at zero as its starting point.
    let minDoses = 0;

    // Loop through the height array to see what the minimum number of doses Dan must take to be able to clear all the hurdles in the race.
    for (let i = 0; i < height.length; i++) {
        // if the max. height that Dan can jump is less than the current height, we are going to add to the minDoses.
        if (k < height[i]) {
            minDoses++;
        }
    }
    return minDoses;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nk = readLine().split(' ');

    const n = parseInt(nk[0], 10);

    const k = parseInt(nk[1], 10);

    const height = readLine().split(' ').map(heightTemp => parseInt(heightTemp, 10));

    let result = hurdleRace(k, height);

    ws.write(result + "\n");

    ws.end();
}
