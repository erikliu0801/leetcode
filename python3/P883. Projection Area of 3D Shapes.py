# ToDo:

"""
883. Projection Area of 3D Shapes
Easy

On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

Note:

    1 <= grid.length = grid[0].length <= 50
    0 <= grid[i][j] <= 50

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
## test part
class Solution:
    def projectionArea(self, grid):
        """
        grid: List[List[int]]
        rtype: int
        """
        
## code here
#1
"""
Wrong Answer
Your input: [[1,2],[3,4,5]]
Output: 24
Expected: 19
"""


class Solution:
    def projectionArea(self, grid):
        zx, xy = 0, 0
        yz = list()
        for x in grid:
            zx += max(x)
            xy += len(x)
            for i, v in enumerate(x):
                try: 
                    if yz[i] < v: yz[i] = v
                except IndexError:
                    yz.append(v)
        return zx + xy + sum(yz)


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [
    [[2]],
    [[1,2],[3,4]],
    [[1,0],[0,2]], 
    [[1,1,1],[1,0,1],[1,1,1]], 
    [[2,2,2],[2,1,2],[2,2,2]]
    ]
    expected_output = [5, 17, 8, 14, 21]
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