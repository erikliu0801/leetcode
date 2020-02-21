# ToDo:

"""
771. Jewels and Stones
Easy

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
## test part
class Solution:
    def numJewelsInStones(self, J, S):
        """
        J: str
        S: str
        rtype: int
        """
        
## code here
#1
"""
Success
Runtime: 12 ms, faster than 99.95% of Python3 online submissions for Jewels and Stones.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
"""
class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        for j in J:
            count += S.count(j)
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