# ToDo:

"""
217. Contains Duplicate
Easy
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
## test part
def containsDuplicate(nums):
	"""
	nums: List[int]
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 120 ms, faster than 97.06% of Python3 online submissions for Contains Duplicate.
Memory Usage: 18.1 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
"""
def containsDuplicate(nums):
	return len(set(nums)) != len(nums)

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