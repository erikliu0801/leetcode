# ToDo:

"""
506. Relative Ranks
Easy

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:

    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        
## test part
def findRelativeRanks(nums):
	"""
	nums: List[int]
	rtype: List[str]
	"""
## code here
#1
"""
Success
Runtime: 348 ms, faster than 22.22% of Python3 online submissions for Relative Ranks.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Relative Ranks.
"""
def findRelativeRanks(nums):
	sorted_nums = nums.copy()
	sorted_nums.sort(reverse=True)
	for i, score in enumerate(nums):
		rank = sorted_nums.index(score) + 1
		if rank == 1:
			nums[i] = "Gold Medal"
		elif rank == 2:
			nums[i] = "Silver Medal"
		elif rank == 3:
			nums[i] = "Bronze Medal"
		else:
			nums[i] = str(rank)
	return nums



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