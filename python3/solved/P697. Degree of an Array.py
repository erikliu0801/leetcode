# ToDo:

"""
697. Degree of an Array
Easy

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
## test part
def findShortestSubArray(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
def findShortestSubArray(nums):
	size = len(nums)
	if size < 2: return size
	if size == 2: return 2 if nums[0] == nums[1] else 1
	from collections import Counter
	n = Counter(nums)
	degrees = []
	min_len = float('inf')
	count = 0
	for k, v in n.most_common():
		if count > v: break 
		else: count = v
		degrees.append(k)
	for degree in degrees:
		l_p = nums.index(degree)
		r_p = nums[::-1].index(degree)
		min_len = min(min_len, size - l_p - r_p)
	return min_len

#1.1
"""
Success
Runtime: 908 ms, faster than 11.30% of Python3 online submissions for Degree of an Array.
Memory Usage: 14.1 MB, less than 36.36% of Python3 online submissions for Degree of an Array.
"""
def findShortestSubArray(nums):
	size = len(nums)
	if size < 2: return size
	from collections import Counter
	n = Counter(nums)
	min_len = float('inf')
	count = 0
	for k, v in n.most_common():
		if count > v: break 
		else: count = v
		l_p = nums.index(k)
		r_p = nums[::-1].index(k)
		min_len = min(min_len, size - l_p - r_p)		
	return min_len


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1, 2, 2, 3, 1], [1,2,2,3,1,4,2]]
	expected_output = [2, 6]
	for i in range(len(input_nums)):
		if findShortestSubArray(input_nums[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', findShortestSubArray(input_nums[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(findShortestSubArray(input_nums[-1]))
	

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