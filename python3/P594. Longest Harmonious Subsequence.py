# ToDo:

"""
594. Longest Harmonious Subsequence
Easy

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].


Note: The length of the input array will not exceed 20,000.
"""
# Conditions & Concepts
"""
harmounious != parlindrome
"""
# Code
## submit part
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
## test part
class Solution:
    def findLHS(self, nums):
        """
        nums: List[int]
        rtype: int
        """

## code here
#1
"""
Wrong Answer
Input: [1,2,3,4]
Output: 1
Expected: 2

Success
Runtime: 6432 ms, faster than 5.15% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 14.6 MB, less than 7.69% of Python3 online submissions for Longest Harmonious Subsequence.
"""
class Solution:
    def findLHS(self, nums):
        elements = set(nums)
        max_lhs_len = 0
        for k in elements:
            if k+1 in elements or k-1 in elements:
                lhs_k = nums.count(k)
                if k+1 in elements:
                    lhs_j = nums.count(k+1)
                else: #k-1 in elements
                    lhs_j = nums.count(k-1)
                max_lhs_len = max(max_lhs_len, lhs_k + lhs_j)

        return max_lhs_len




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