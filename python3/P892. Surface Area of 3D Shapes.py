# ToDo:

"""
892. Surface Area of 3D Shapes
Easy

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10

Example 2:

Input: [[1,2],[3,4]]
Output: 34

Example 3:

Input: [[1,0],[0,2]]
Output: 16

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

Note:

    1 <= N <= 50
    0 <= grid[i][j] <= 50

"""
# Conditions & Concepts
"""
Extends P883. Projection Area of 3D Shapes

def projectionArea(grid):
    zx, xy = 0, 0
    yz = list()
    for x in grid:
        zx += max(x)
        for i, v in enumerate(x):
            if v != 0: xy += 1
            try: 
                if yz[i] < v: yz[i] = v
            except IndexError:
                yz.append(v)
    return zx + xy + sum(yz)

"""
# Code
## submit part
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
## test part
def surfaceArea(grid):
    """
    grid: List[List[int]]
    rtype: int:
    """

## code here
#1 extends P883. Projection Area of 3D Shapes
"""
Wrong Answer
Your input : [[1,1,1],[1,0,1],[1,1,1]]
Output: 28
Expected: 32

Wrong Answer
Runtime: 32 ms
Your input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 42
Expected: 46
"""
def surfaceArea(grid):
    zx, xy = 0, 0
    yz = list()
    for x in grid:
        zx += max(x)
        for i, v in enumerate(x):
            if v != 0: xy += 1 # here more?
            try: 
                if yz[i] < v: yz[i] = v
            except IndexError:
                yz.append(v)
    return (zx + xy + sum(yz))*2

#1.1
def surfaceArea(grid):


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