# ToDo:

"""
665. Non-decreasing Array
Easy

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
## test part
def checkPossibility(nums):
	"""
	nums: List[int]
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input: [2,3,3,2,4]
Output: false
Expected: true

Success
Runtime: 212 ms, faster than 37.06% of Python3 online submissions for Non-decreasing Array.
Memory Usage: 14 MB, less than 93.33% of Python3 online submissions for Non-decreasing Array.
"""
def checkPossibility(nums):
	nums0 = nums.copy()
	for i in range(1,len(nums)):
		if nums[i] < nums[i-1]:
			nums[i-1] = nums[i]
			new_nums_sorted = nums.copy()
			new_nums_sorted.sort()
			nums0[i] = nums0[i-1]
			new_nums0_sorted = nums0.copy()
			new_nums0_sorted.sort()
			return nums == new_nums_sorted or nums0 == new_nums0_sorted
	return True

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1,2,3],[4,2,3],[4,2,1],[3,4,2,3],[2,3,3,2,4]]
	expected_output = [True, True, False, False, True]
	for i in range(len(input_nums)):
		if checkPossibility(input_nums[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', checkPossibility(input_nums[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(checkPossibility(input_nums[-1]))
	

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