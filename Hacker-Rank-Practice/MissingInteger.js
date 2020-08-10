// Write a function:
​
// function solution(A);
​
// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
​
// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
​
// Given A = [1, 2, 3], the function should return 4.
​
// Given A = [−1, −3], the function should return 1.
​
// Write an efficient algorithm for the following assumptions:
​
//N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].
​
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
​
function solution(A) {
    // A = the given array
    // N = number of integers
    // Goal: We need to return the smallest positive integer, greater than 0, that does not appear in the array.
    
    let length = A.length;
    let array = Array(length).fill(false);
    
    for (let i = 0; i < length; i++) {
        if (A[i] < 1 || A[i] > length) {
            continue;
        }
        array[A[i] - 1] = true;
    }
    for (let i = 0; i < length; i++) {
        if (!array[i]) {
            return i + 1;
        }
    }
    return length + 1;
   
}
​
// assert.strictEqual(solution([2, 4, 5]), 1);