# ToDo:

"""
349. Intersection of Two Arrays
Easy
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
## test part
def intersection(nums1, nums2):
	"""
	nums1: List[int]
	nums2: List[int]
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 44 ms, faster than 85.72% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.
"""
def intersection(nums1, nums2):
	return list(set(nums1)&set(nums2))


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