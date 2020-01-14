# ToDo:

"""
167. Two Sum II - Input array is sorted
Easy

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
## test part
def twoSum(numbers, target):
	"""
	numbers: List[int]
	target: int
	rtype: List[int]
	"""
## code here
#1
"""
Input:[0,0,3,4],0
Output:[1,1]
Expected:[1,2]

Success
Runtime: 2892 ms, faster than 5.01% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.
"""
def twoSum(numbers, target):
	for i, num in enumerate(numbers):
		rest = target - num
		if rest in numbers[i+1:]:
			return [i+1, numbers[i+1:].index(rest) + i + 2]
		if rest < 0:
			return []

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