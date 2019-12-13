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
	def findAverage(nums):
		nums_sum = 0
		for j in nums:
			nums_sum += j
		nums_average = nums_sum / len(nums)
		return nums_average
	def discreteList(nums, nums_average):
		for i in range(len(nums)):
			nums[i] = nums[i] - nums_average
		return nums
	
	
# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_nums = [
		[-2,1,-3,4,-1,2,1,-5,4]
	]
    expected_output = [6 ]
	expected_nums = [
		[4,-1,2,1]
	]

    for i, j in enumerate(input1):
        if maxSubArray(input_nums[i]) != expected_output[i]:
            print("Wrong!!!")
            print(maxSubArray(input_nums[i]))
        else:            
            print("Right")
    # print(maxSubArray(input_nums[1]))
	

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