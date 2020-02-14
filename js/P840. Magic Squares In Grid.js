// ToDo:
/* */

// Problem Description
/*
840. Magic Squares In Grid
Easy

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).


Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    0 <= grid[i][j] <= 15
*/

// Conditions & Concepts
/*


*/

// Code
// submit part
/**
 * @param {number[][]} grid
 * @return {number}
 */

// code here
// 1
/* */
var numMagicSquaresInside = function(grid) {
    var rows = grid.length;
    var cols = grid[0].length;
    if (rows < 3 | cols < 3) {
    	return 0
    };
    var p = 0;
    var diagonals = [grid[0][0], grid[0][-1]]
    for (var row =0; row < rows; row++) {
    	for (var col = 0; col < cols; col++) {

    	}
    }
};

// Test
