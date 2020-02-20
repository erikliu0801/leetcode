# ToDo:

"""
645. Set Mismatch
Easy

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Note:

    The given array size will in the range [2, 10000].
    The given array's numbers won't have any order.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
## test part
class Solution:
    def findErrorNums(self, nums):
        """
        nums: List[int]
        rtype: List[int]
        """

## code here
#1
"""
Wrong Answer
Input: [1,1]
Output: [1]
Expected: [1,2]

Success
Runtime: 212 ms, faster than 60.44% of Python3 online submissions for Set Mismatch.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Set Mismatch.
"""
class Solution:
    def findErrorNums(self, nums):
        repetition = []
        missing = []
        nums.sort()
        pre = 0
        for c in nums:
            if c != pre +1:
                if c == pre: 
                    if c not in repetition:
                        repetition.append(c)
                    continue
                else:
                    while pre + 1 != c:
                        pre += 1
                        missing.append(pre)
            pre = c
        if not missing: missing = [pre+1]
        return repetition + missing

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [[1,2,2,4], [1,2,2,2,4], [1,2,2,2,5]]
    expected_output = [[2,3], [2,3], [2,3,4]]
    for i in range(len(input1)):
        if findErrorNums(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findErrorNums(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(findErrorNums(input1[-1]))
    

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