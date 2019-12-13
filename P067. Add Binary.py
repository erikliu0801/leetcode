# ToDo:

"""
67. Add Binary
Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def addBinary(self, a: str, b: str) -> str:
## test part
def addBinary(a, b):
	"""
	a: str
	b: str
	rtype: str
	"""
## code here
#1
def addBinary(a, b):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_str_a = ["11", "1010"]
	input_str_b = ["1", "1011"]
	expected_output = ["100", "10101"]
	for i in range(len(input1)):
		if addBinary(input_str_a[i], input_str_b[i]) != expected_output[i]:
			print("Wrong!!!")
			print(addBinary(input_str_a[i], input_str_b[i])
		else:
			print("Right")		
	# print(addBinary(input_str_a[i], input_str_b[i]))
	

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