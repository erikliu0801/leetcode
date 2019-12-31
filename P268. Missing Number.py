# ToDo:

"""268. Missing Number
Easy
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
## test part
def missingNumber(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
"""
Runtime Error
Last executed input: [0]

Success
Runtime: 148 ms, faster than 64.16% of Python3 online submissions for Missing Number.
Memory Usage: 14.8 MB, less than 6.45% of Python3 online submissions for Missing Number.
"""
def missingNumber(nums):
	nums = set(nums)
	complete_nums = set(range(0,max(nums)))
	missing_nums = complete_nums - nums
	if missing_nums == set():
		return max(nums) +1
	return missing_nums.pop()

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
			print("Wrong!!!")
			print(func(input1[i]))
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