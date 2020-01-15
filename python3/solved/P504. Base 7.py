# ToDo:

"""
504. Base 7
Easy

Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"

Example 2:

Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7]. 

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def convertToBase7(self, num: int) -> str:
        
## test part
def convertToBase7(num):
	"""
	num: int
	rtype: str
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 60.77% of Python3 online submissions for Base 7.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Base 7.
"""
def convertToBase7(num):	
	negative = False
	if num < 0:
		negative = True
		num = abs(num)
	elif  num == 0:
		return '0'
	import math
	digits = int(math.log(num,7))
	sevenbasenum = ''
	while digits != -1:
		sevenbasenum = sevenbasenum + str(num//(7**digits))
		num = num % (7**digits)
		digits -= 1
	if negative:
		return '-' + sevenbasenum
	return sevenbasenum


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