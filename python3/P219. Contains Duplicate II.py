# ToDo:

"""
219. Contains Duplicate II
Easy
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
## test part
def containsNearbyDuplicate(nums, k):
	"""
	nums: List[int]
	k: int
	rtype: bool
	"""
## code here
#1
def containsNearbyDuplicate(nums, k):

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