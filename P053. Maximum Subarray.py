# ToDo:

"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""
# Concepts


# Code
## submit part
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
## test part
def maxSubArray(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
def maxSubArray(nums):

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input1 = []
	expected_output = []
	for i, j in enumerate(input1):
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