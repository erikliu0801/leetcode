# ToDo:

"""
1047. Remove All Adjacent Duplicates In String
Easy

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Note:

    1 <= S.length <= 20000
    S consists only of English lowercase letters.

Hint:
    Use a stack to process everything greedily.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
## test part
class Solution:
    def removeDuplicates(self, S):
        """
        S: str
        rtype: str
        """
        
## code here
#1
"""
Success
Runtime: 64 ms, faster than 92.35% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
"""
class Solution:
    def removeDuplicates(self, S):
        res = ""
        for c in S:
            if res:
                if c == res[-1]:
                    res = res[:-1]
                    continue
            res += c
        return res


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = ["abbaca", "abbbaca"]
    expected_output = ["ca", "abaca"]
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