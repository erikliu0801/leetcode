# ToDo:

"""
812. Largest Triangle Area
Easy

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.

Notes:

    3 <= points.length <= 50.
    No points will be duplicated.
     -50 <= points[i][j] <= 50.
    Answers within 10^-6 of the true value will be accepted as correct.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
## test part
class Solution:
    def largestTriangleArea(self, points):
        """
        points: List[List[int]]
        rtype: float
        """
        
## code here
#1
"""
Success
Runtime: 116 ms, faster than 79.67% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Largest Triangle Area.
"""
class Solution:
    def largestTriangleArea(self, points):
        from itertools import combinations
        res = 0
        for p in combinations(points,3):
            a, b, c = p
            area = abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]))/2
            if area > res: res = area
        return res



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