# ToDo:

"""
628. Maximum Product of Three Numbers
Easy

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Note:

    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
## test part
def maximumProduct(nums):
	"""
	nums: List[int]
	rtpye: int
	"""
## code here
#1
"""
Success
Runtime: 288 ms, faster than 34.88% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Maximum Product of Three Numbers.
"""
def maximumProduct(nums):
	nums.sort(reverse=True)
	a, b, c, *_ = nums
	*_, d, e = nums
	return max(a*b*c, a*d*e)

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1,2,3], [1,2,3,4]]
	expected_output = [6, 24]
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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