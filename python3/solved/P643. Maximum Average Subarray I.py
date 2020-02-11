# ToDo:

"""
643. Maximum Average Subarray I
Easy

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
## test part
def findMaxAverage(nums, k):
	"""
	nums: List[int]
	k: int
	rtype: float
	"""
## code here
#1
# def findMaxAverage(nums, k):
# 	if k == 1:
# 		return max(nums)
# 	import numpy as np
# 	probatility = len(nums) - k + 1
# 	max_sum = float('-inf')
# 	for i in range(probatility):
# 		max_sum = max(max_sum, np.mean(nums[i:k+i]))
# 	return max_sum

#1.1
"""
Success
Runtime: 928 ms, faster than 56.20% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 16 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.
"""
def findMaxAverage(nums, k):
	if k == 1: return max(nums)
	max_sum = sum(nums[:k])/k	
	rest_prob = len(nums) - k
	mean = max_sum
	for i in range(rest_prob):
		mean += (nums[k+i] - nums[i]) / k
		max_sum = max(max_sum, mean)
	return max_sum


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1,12,-5,-6,50,3]]
	input_k = [4]
	expected_output = [12.75]
	for i in range(len(input_nums)):
		if findMaxAverage(input_nums[i], input_k[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', findMaxAverage(input_nums[i], input_k[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(findMaxAverage(input_nums[-1], input_k[-1]))
	

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