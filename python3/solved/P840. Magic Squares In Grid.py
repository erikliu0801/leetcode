# ToDo:

"""
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
"""
# Conditions & Concepts
"""
1. distinct 1~9
2. sum of all columns, rows and both diagonals are same
"""
# Code
## submit part
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
## test part
def numMagicSquaresInside(grid):
    """
    grid: List[List[int]])
    rtype: int:
    """

## code here
#1
"""
Success
Runtime: 52 ms, faster than 24.04% of Python3 online submissions for Magic Squares In Grid.
Memory Usage: 14.1 MB, less than 11.40% of Python3 online submissions for Magic Squares In Grid.
"""
def numMagicSquaresInside(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    if rows < 3 or cols < 3: return 0
    for r in range(rows-2):
        for c in range(cols-2):

            # origin = (r,c)
            r1 = [grid[r][c], grid[r][c+1], grid[r][c+2]]
            r2 = [grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]]
            r3 = [grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]]
            c1 = [grid[r][c], grid[r+1][c], grid[r+2][c]]
            c2 = [grid[r][c+1], grid[r+1][c+1], grid[r+2][c+1]]
            c3 = [grid[r][c+2], grid[r+1][c+2], grid[r+2][c+2]]
            d1 = [grid[r][c], grid[r+1][c+1], grid[r+2][c+2]]
            d2 = [grid[r][c+2], grid[r+1][c+1], grid[r+2][c]]

            nums = r1 + r2 + r3
            if len(nums) != len(set(nums)): continue
            if sorted(nums) != [i for i in range(1,10)]: continue
            if sum(r1) != 15 or \
               sum(r2) != 15 or \
               sum(r3) != 15 or \
               sum(c1) != 15 or \
               sum(c2) != 15 or \
               sum(c3) != 15 or \
               sum(d1) != 15 or \
               sum(d2) != 15: continue

            count += 1
    return count


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = []
    expected_output = []
    for i in range(len(input1)):
        if func(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(func(input1[-1]))
    

## Performance Test
import cProfile
cProfile.run('')


## Unit Test
import unittest
class Test(unittest.TestCase):
    def test(self):
        pass

if __name__ == '__main__':
unittest.main()