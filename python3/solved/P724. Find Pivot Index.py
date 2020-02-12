# ToDo:

"""
724. Find Pivot Index
Easy

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs. 

Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement. 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
## test part
def pivotIndex(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 9404 ms, faster than 5.00% of Python3 online submissions for Find Pivot Index.
Memory Usage: 14 MB, less than 83.33% of Python3 online submissions for Find Pivot Index.
"""
def pivotIndex(nums):
	for i in range(len(nums)):
		if sum(nums[:i]) == sum(nums[i+1:]): return i
	return -1


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [1,2,-2]]
	expected_output = [3, -1, 0]
	for i in range(len(input_nums)):
		if pivotIndex(input_nums[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', pivotIndex(input_nums[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(pivotIndex(input_nums[-1]))
	

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