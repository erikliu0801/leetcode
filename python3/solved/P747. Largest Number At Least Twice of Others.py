# ToDo:

"""
747. Largest Number At Least Twice of Others
Easy

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
## test part
def dominantIndex(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
"""
Runtime Error: ValueError: max() arg is an empty sequence
Last executed input: [1]

Success
Runtime: 32 ms, faster than 80.92% of Python3 online submissions for Largest Number At Least Twice of Others.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Largest Number At Least Twice of Others.
"""
def dominantIndex(nums):
	if len(nums) < 2: return 0
	a = max(nums)
	i = nums.index(a)
	nums.remove(a)
	return i if a >= (max(nums)*2) else -1


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[3, 6, 1, 0], [1, 2, 3, 4], [0,0,0,1]]
	expected_output = [1, -1, 3]
	for i in range(len(input_nums)):
		if dominantIndex(input_nums[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', dominantIndex(input_nums[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(dominantIndex(input_nums[-1]))
	

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