# ToDo:

"""
283. Move Zeroes
Easy

2707

96

Add to List

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
## test part
def moveZeroes(nums):
	"""
	nums: List[int]
	rtype: None
	"""
## code here
#1
"""
Time Limit Exceeded
Last executed input: [0,0]

Wrong Answer
Input: [2,1]
Output: [1,2]
Expected: [2,1]

Misunderstanding
"""
def moveZeroes(nums):
	if len(nums) not in [0,1]:
		nums.sort()
		for _ in range(nums.count(0)):
			nums.pop(0)
			nums.append(0)

#1.1
"""
Success
Runtime: 96 ms, faster than 21.83% of Python3 online submissions for Move Zeroes.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
"""
def moveZeroes(nums):
	if len(nums) not in [0,1]:
		for _ in range(nums.count(0)):
			nums.remove(0)
			nums.append(0)


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