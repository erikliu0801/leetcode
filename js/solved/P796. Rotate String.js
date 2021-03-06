// ToDo:
/* */

// Problem Description
/*
796. Rotate String
Easy

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
*/

// Conditions & Concepts
/* 
1. A.length == B.length

*/

// Code
// submit part
/**
 * @param {string} A
 * @param {string} B
 * @return {boolean}
 */
var rotateString = function(A, B) {
    
};

// test part
/* */

// code here
// 1
/*
Success
Runtime: 68 ms, faster than 13.97% of JavaScript online submissions for Rotate String.
Memory Usage: 36.2 MB, less than 50.00% of JavaScript online submissions for Rotate String.
*/
var rotateString = function(A, B) {
    if (A.length !== B.length) {return false}

    A = A.split("")
    B = B.split("")

    var i = 0
    do {
        if (JSON.stringify(A) === JSON.stringify(B)) {return true} //arrayA == arrayB is disgusting

        A.push(A[0])
        A.shift()

        i++
    } while (i < A.length)

    return false
};

// 1.1

// Test
