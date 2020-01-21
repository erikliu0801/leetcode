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
2. m+n <= len(nums1+nums2) => Misunderstanding!!
2.1 m+n <= len(nums1)

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
"""
Misunderstanding
"""
def merge(nums1, m, nums2, n):
	nums1, nums2, i = nums1[:m], nums2[:n], 0
	while nums2 != []:
		if nums1[i] >= nums2[0]:
			nums1.insert(i, nums2[0])
			nums2 = nums2[1:]
		i +=1
		if i == len(nums1):
			break
	nums1 = nums1 + nums2
	return nums1

#2
def merge(nums1, m, nums2, n):
	nums2, i = nums2[:n], 0
	temp_num = nums1[0]
	for i in range(len(nums1)-m):
		nums1[-1-i] = 0
	while nums2 != []:
		if nums1[i] >= nums2[0] or nums1[i] == 0:
			nums1.insert(i, nums2[0])
			nums1.pop()
			num2 = nums2[1:]
	return nums1

#3 new
def merge(nums1, m, nums2, n):
	i = 0
	for j in range(n):
		while nums2[j] > nums1[i] and i < m + j:
			i += 1
		nums1.insert(i, nums2[j])
		nums1.pop()
	return nums1

#3.1
"""
Runtime Error

[0],0
[1],1
"""
def merge(nums1, m, nums2, n):
	i = 0
	for j in range(n):
		if i+1 >= m + j:
			nums1[i+1] = nums2[j]
			i += 1
			continue
		while nums2[j] > nums1[i] and i < m + j:
			i += 1
		nums1.insert(i, nums2[j])
		nums1.pop()

#4
"""
Success
Runtime: 24 ms, faster than 99.48% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""
def merge(nums1, m, nums2, n):
	nums2 = nums1[:m] + nums2[:n]
	nums2.sort()
	for i in range(m+n):
		nums1[i] = nums2[i]
	return nums1

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums1 = [
	[[1,2,3,0,0,0], 3],
	[[1,2,3,7,0,0], 3],
	[[1,2,3,7,0,0], 2],
	[[1,2,3,4,0,0,0],4],
	[[1,2,3,0,0,0], 2],
	[[0],0]
	]
	input_nums2 = [
	[[2,5,6], 3],
	[[2,5,6], 3],
	[[2,5,6,8], 4],
	[[2,5,6],2],
	[[2,5,6], 3],
	[[1],1]
	]
	expected_output = [
	[1,2,2,3,5,6],
	[1,2,2,3,5,6],
	[1,2,2,5,6,8],
	[1,2,2,3,4,5,0],
	[1,2,2,5,6,0],
	[1]
	]

	# for i in range(len(input_nums1)):
	# 	if merge(input_nums1[i][0],input_nums1[i][1],input_nums2[i][0],input_nums2[i][1]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(merge(input_nums1[i][0],input_nums1[i][1],input_nums2[i][0],input_nums2[i][1]))
	# 	else:
	# 		print("Right")		
	print(merge(input_nums1[-1][0],input_nums1[-1][1],input_nums2[-1][0],input_nums2[-1][1]))
	

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