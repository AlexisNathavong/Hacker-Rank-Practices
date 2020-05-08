// Problem:
// We are given a list of frequencies and a list of filter ranges. Our goal is to 
// determine how many of our given frequencies will pass through all of these 
// filters successfully.

// FIRST-PASS SOLUTION

// High-level approach:
// We want to look at each frequency in our list and evaluate it against each of the
// filters by checking if it falls within the range's upper and lower bounds.
// If the frequency passes all the filters, we'll increment a counter tracking
// how many frequencies can make it through the filter ranges.

// Step by step:
// 1. Define a counter to track how many frequencies can pass all filters
// 2. Use a for-loop to iterate over the filter array
// 3. Define a counter to track how many filters each frequency can pass
// 4. For each frequency, use a for-loop to iterate over the filters array
// 5. For each filter, check if the frequency falls within the given range
    // if yes, iterate the counter in step 3
// 6. Check to see if counter in step 3 === length of filter array
    // if yes, this means the frequency passed all filters
        // iterate counter in step 1
// 7. Return counter in step 1

// Runtime: 
// O(n * m) where n = length of frequency array, m = length of filter array
// Roughly the same as O(n^2)

function countSignals(frequencies, filterRanges) {
  // counter for signals that pass all filters
  let numSignals = 0;

  // loop through frequencies 
  for(let i = 0; i < frequencies.length; i++) {
    // counter for num of filters frequency passes
    let filtersPassed = 0
    // loop through filter ranges
    for(let j = 0; j < filterRanges.length; j++) {
      // check frequency against each range
      if(frequencies[i] >= filterRanges[j][0] && frequencies[i] <= filterRanges[j][1]) {
        filtersPassed++;
      }
    }

    // check if frequency passes all filters
    if(filtersPassed === filterRanges.length) {
      numSignals++
    }
  }
  return numSignals
}


// OPTIMIZED SOLUTION

// High-level approach:
// First we find a range at which all of the filters overlap.
// If a frequency fits through this range, it will pass all filters by default.
// Loop through the frequencies and check each against this overlap range.

// Step by step:
// 1. Define a counter to track how many frequencies can pass all filters
// 2. Define the overlap range, initialize it to the first filter range in the array
// 3. Use a for-loop to check the remaining filter ranges against the overlap range
    // if the lower bound in a range is larger than that of the overlap range:
        // replace overlap range lower bound with this new value
    // if the upper bound in a range is smaller than that of the overlap range:
        // replace overlap range upper bound with this new value
// 4. Use a for-loop to iterate over the frequency array
// 5. For each frequency, check if it falls inside our new overlap range
    // if yes, iterate the counter in step 1
// 6. Return the counter in step 1  

// Runtime: 
// O(n + m) where n = length of frequency array, m = length of filter array
// Roughly the same as O(2n) or O(n)

function betterCount(freqs, ranges) {
  // counter for signals that pass all filters
  let numSignals = 0;

// initialize the overlap range
  let limitRange = [ranges[0][0], ranges[0][1]]

  // loop over filter array and check for updates to overlap range
  for(let i = 1; i < ranges.length; i++) {
    if(ranges[i][0] > limitRange[0]) {
      limitRange[0] = ranges[i][0]
    }

    if(ranges[i][1] < limitRange[1]) {
      limitRange[1] = ranges[i][1]
    }
  }

  // loop over frequency array and check if each passes through our overlap range
  for(let i = 0; i < freqs.length; i++) {
    if(freqs[i] >= limitRange[0] && freqs[i] <= limitRange[1]) {
      numSignals++
    }
  }

  return numSignals
}

const freqs = [20, 5, 6, 7, 12]

const ranges = [[10,20], [5,15], [5,30]]

console.log(countSignals(freqs, ranges))

console.log(betterCount(freqs, ranges))