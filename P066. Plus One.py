# ToDo:

"""
66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
# Conditions & Concepts
"""
1. array : non-empty, non-negative integer

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
"""
Success
Runtime: 28 ms, faster than 92.55% of Python3 online submissions for Plus One.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Plus One.
"""
def plusOne(digits):
	digits[-1] = digits[-1] + 1
	if digits[-1] >= 10:
		digits[-1] = digits[-1] -10
		carry = 1
		position = 1
		while carry == 1:
			if position > len(digits):
				digits = [1] + digits
				position += 1
			else:
				position += 1
				digits[0-position] = digits[0-position] + carry
				if digits[-1] >= 10:
					digits[-1] = digits[-1] -10
					carry = 1
				else:
					carry = 0
	return digits



# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_digits = [
	[1,2,3],
	[4,3,2,1],
	[9,9,9],
	[0],
	[9,8,9]
	]
	expected_output = [
	[1,2,4],
	[4,3,2,2],
	[1,0,0,0]
	[1],
	[9,9,0]
	]
	for i in range(len(input_digits)):
		if plusOne(input_digits[i]) != expected_output[i]:
			print("Wrong!!!")
			print(plusOne(input_digits[i]))
		else:
			print("Right")
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