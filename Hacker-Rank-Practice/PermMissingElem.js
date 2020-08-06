// Task description
// An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
// Your goal is to find that missing element.
// Write a function:
// function solution(A);
// that, given an array A, returns the value of the missing element.
// For example, given array A such that:
//   A[0] = 2
//   A[1] = 3
//   A[2] = 1
//   A[3] = 5
// the function should return 4, as it is the missing element.
// Write an efficient algorithm for the following assumptions:
// N is an integer within the range [0..100,000];
// the elements of A are all distinct;
// each element of array A is an integer within the range [1..(N + 1)].

// A = the given array with no duplicates
// return the missing element from the array
// array is 1 to n+1
function solution(A) {
    // use the formula of First Natural Numbers
    // loop through the length of the array, subtract A[i] from the sum of the formula
    // return the result
    let n = A.length;
    let missingElement = (n + 1) * (n + 2) / 2;
    for (let i = 0; i < n; i++) {
        missingElement -= A[i];
    }
    return missingElement;
}