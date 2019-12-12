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
def searchInsert(nums, target):

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
	for i, j in enumerate(input1):
		if searchInsert(input1[i]) != expected_output[i]:
			print("Wrong!!!")
			print(searchInsert(input1[i]))
		else:
			print("Right")		
	# print(searchInsert(input1[-1]))
	

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