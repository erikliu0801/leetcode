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
"""
Wrong Answer
Input: 0
Output: false
Expected: true

Success
Runtime: 356 ms, faster than 21.00% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sum of Square Numbers.
"""
class Solution:
    def judgeSquareSum(self, c):
        import math
        limit = math.sqrt(2) / 2
        for a in range(int(c * limit) + 1):
            if a ** 2 > c: break
            if math.sqrt(abs(c - a ** 2)) % 1 == 0: return True
        return False


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [5, 3]
    expected_output = [True, False]
    for i in range(len(input1)):
        if judgeSquareSum(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', judgeSquareSum(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(judgeSquareSum(input1[-1]))
    

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