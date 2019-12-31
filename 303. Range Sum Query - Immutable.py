# ToDo:

"""
303. Range Sum Query - Immutable
Easy
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class NumArray:

	def __init__(self, nums: List[int]):
		

	def sumRange(self, i: int, j: int) -> int:
	 
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
## test part

## code here
#1
"""
Success
Runtime: 1380 ms, faster than 5.40% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.
"""
class NumArray:
	def __init__(self, nums: List[int]):
		self.num_array = nums
	def sumRange(self, i: int, j: int) -> int:
		return sum(self.num_array[i:j+1])

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