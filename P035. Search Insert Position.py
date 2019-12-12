# ToDo:

"""
35. Search Insert Position
Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

"""
# Concepts


# Code
## submit part
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
## test part
def searchInsert(nums, target):
	"""
	nums: List[int]
	target: int
	rtype: int
	"""

## code here
#1
"""
Success
Runtime: 52 ms, faster than 80.69% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
"""
def searchInsert(nums, target):	
	if len(nums) == 0:
		return 0
	else:
		if target < nums[0]:
			return 0
		elif target > nums[-1]:
			return len(nums)
		else:
			for i in range(len(nums)):
				if nums[i] == target:
					return i
				elif target < nums[i]:
					return i

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_nums = [
	[1,3,5,6],
	[1,3,5,6],
	[1,3,5,6],
	[1,3,5,6]
	]
	input_target = [5,2,7,0]
	expected_output = [2,1,4,0]
	for i, j in enumerate(input_nums):
		if searchInsert(input_target[i],expected_output[i]) != expected_output[i]:
			print("Wrong!!!")
			print(searchInsert(input_target[i],expected_output[i]))
		else:
			print("Right")		
	# print(searchInsert(input_target[-1],expected_output[-1]))
	

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