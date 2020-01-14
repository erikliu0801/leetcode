# ToDo:

"""
350. Intersection of Two Arrays II
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
## test part
def intersect(nums1, nums2):
	"""
	nums1: List[int]
	nums2: List[int]
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 64 ms, faster than 24.35% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
"""
def intersect(nums1, nums2):
	instersect_nums = list()
	for instersect_num in set(nums1)&set(nums2):
		for _ in range(min(nums1.count(instersect_num),nums2.count(instersect_num))):
			instersect_nums.append(instersect_num)
	return instersect_nums



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