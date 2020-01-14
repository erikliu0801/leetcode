# ToDo:

"""
367. Valid Perfect Square
Easy
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		
## test part
def isPerfectSquare(num):
	"""
	num: int
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 16 ms, faster than 99.75% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Valid Perfect Square.
"""
def isPerfectSquare(num):
	import math
	return math.sqrt(num)%1 == 0

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