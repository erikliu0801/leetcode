# ToDo:

"""
P970. Powerful Integers
Easy

Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once. 


Example 2:
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Note:
    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
## test part
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        x: int
        y: int
        bound: int
        rtype: List[int]
        """
        
## code here
#1
"""
Time Limit Exceeded
Last executed input: 2, 1, 10
"""
class Solution:
    def powerfulIntegers(self, x, y, bound):
        res = set()
        i = 0

        while x**i <= bound:
            j = 0
            base = x**i
            while base + y**j <= bound:
                res.add(base + y**j)
                j += 1
            i += 1
        return list(res)

#1.1
"""
Success
Runtime: 20 ms, faster than 96.83% of Python3 online submissions for Powerful Integers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Powerful Integers.
"""
class Solution:
    def powerfulIntegers(self, x, y, bound):
        if bound < 2: return []
        if x == 1 and y == 1: return [2]
        if y == 1: x, y = y, x

        res = set()
        i = 0
        while x**i <= bound:
            j = 0
            base = x**i
            while base + y**j <= bound:
                res.add(base + y**j)
                j += 1
            if x == 1: break
            i += 1
        res = list(res)
        return res


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [2, 3, 1]
    input2 = [3, 5, 1]
    input3 = [100, 15, 3]
    expected_output = [[2,3,4,5,7,9,10], [2,4,6,8,10,14], []]
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