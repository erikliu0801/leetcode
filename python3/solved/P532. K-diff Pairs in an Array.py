# ToDo:

"""
532. K-diff Pairs in an Array
Easy

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
## test part
def findPairs(nums, k):
	"""
	nums: List[int]
	k: int
	rtype: int
	"""
## code here
#1
def findPairs(nums, k):
	nums.sort()
	checked = set()
	count = 0
	if k > 0:
		for num in nums:
			if (num not in checked) and (num+k in nums):
				count += 1
			checked.add(num)
	elif k == 0:
		for num in set(nums):
			if nums.count(num) > 1:
				count += 1
	return count

#1.1
"""
Success
Runtime: 124 ms, faster than 92.26% of Python3 online submissions for K-diff Pairs in an Array.
Memory Usage: 14.5 MB, less than 83.87% of Python3 online submissions for K-diff Pairs in an Array.
"""
def findPairs(nums, k):
	s = set(nums)
	count = 0
	if k > 0:
		for e in s:
			if e + k in s:
				count += 1
	elif k == 0:
		for e in s:
			if nums.count(e) > 1:
				count += 1
	return count


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[3, 1, 4, 1, 5], [1, 2, 3, 4, 5], [1, 3, 1, 5, 4], [1, 3, 1, 5, 4, 1, 1]]
	input_k = [2, 1, 0, 0]
	expected_output = [2, 4, 1, 1]
	for i in range(len(input_nums)):
		if findPairs(input_nums[i], input_k[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', findPairs(input_nums[i], input_k[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(findPairs(input_nums[-1], input_k[-1]))
	

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