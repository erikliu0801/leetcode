# ToDo:

"""
633. Sum of Square Numbers
Easy
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:
Input: 3
Output: False
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
## test part
class Solution:
    def judgeSquareSum(self, c):
        """
        c: int
        rtype: bool:
        """
        
## code here
#1
class Solution:
    def judgeSquareSum(self, c):
        import math
        limit = math.sqrt(2)/2
        for a in range(1, int(c * limit) +1):
            if math.sqrt(c - a**2) % 1 == 0: return True
        return False



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