# ToDo:

"""
704. Binary Search
Easy

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
## test part
def search(nums, target):
	"""
	nums: List[int]
	target: int) -> int
	"""
## code here
#1
"""
Success
Runtime: 252 ms, faster than 94.67% of Python3 online submissions for Binary Search.
Memory Usage: 14 MB, less than 87.10% of Python3 online submissions for Binary Search.
"""
def search(nums, target):
	if target in nums:
		return nums.index(target)
	return -1

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[-1,0,3,5,9,12], [-1,0,3,5,9,12]]
	input_target = [9, 2]
	expected_output = [4, -1]
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