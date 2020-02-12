# ToDo:

"""
674. Longest Continuous Increasing Subsequence
Easy

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Note: Length of the array will not exceed 10,000. 

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
## test part
def findLengthOfLCIS(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
"""
Runtime Error
Last executed input: [1,3,5,7]

Runtime Error
Last executed input: [1]

Success
Runtime: 72 ms, faster than 93.67% of Python3 online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 13.9 MB, less than 95.65% of Python3 online submissions for Longest Continuous Increasing Subsequence.
"""
def findLengthOfLCIS(nums):
	if len(nums) < 2:
		return len(nums)
	count = 1
	nums_count = []
	for i in range(1,len(nums)):
		if nums[i] > nums[i-1]:
			count += 1
			if i == len(nums) -1:
				nums_count.append(count)
		else:
			nums_count.append(count)
			count = 1
	return max(nums_count)


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1,3,5,4,7], [2,2,2,2,2], [1,3,5,7], [1]]
	expected_output = [3, 1, 4, 1]
	for i in range(len(input_nums)):
		if findLengthOfLCIS(input_nums[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', findLengthOfLCIS(input_nums[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(findLengthOfLCIS(input_nums[-1]))
	

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