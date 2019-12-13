# ToDo:

"""
66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


"""
# Concepts
"""

"""
# Code
## submit part
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
## test part
def plusOne(digits):
	"""
	digits: List[int]
	rtype: List[int]
	"""
## code here
#1
def plusOne(digits):
	"""
	digits: List[int]
	rtype: List[int]
	"""

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_digits = [
	[1,2,3]
	]
	expected_output = [
	[1,2,4]
	]
	for i, j in enumerate(input_digits):
		if plusOne(input_digits[i]) != expected_output[i]:
			print("Wrong!!!")
			print(plusOne(input_digits[i]))
		else:
			plusOne("Right")
	# print(plusOne(input_digits[-1]))
	

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