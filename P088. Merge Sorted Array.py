# ToDo:

"""
88. Merge Sorted Array
Easy
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""
# Conditions & Concepts
"""
1. already sorted
2. m+n <= len(nums1+nums2)

"""
# Code
## submit part
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
## test part
def merge(nums1, m, nums2, n):
	"""
	nums1: List[int]
	m: int
	nums2: List[int]
	n: int
	rtype: None
	"""
## code here
#1
def merge(nums1, m, nums2, n):
	nums1, nums2, i = nums1[:m], nums2[:n], 0
	while nums2 != []:
		if nums1[i] >= nums2[0]:
			nums1.insert(i, nums2[0])
			nums2 = nums2[1:]
		i +=1
	return nums1


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