# ToDo:

"""
448. Find All Numbers Disappeared in an Array
Easy
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
## test part
def findDisappearedNumbers(nums):
	"""
	nums: List[int]
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 368 ms, faster than 79.19% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.1 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
def findDisappearedNumbers(nums):
	return list(set(x for x in range(1,len(nums)+1))-set(nums))

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