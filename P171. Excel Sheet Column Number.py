# ToDo:

"""
171. Excel Sheet Column Number
Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701
"""
# Conditions & Concepts
"""
trans P168
"""
# Code
## submit part
class Solution:
    def titleToNumber(self, s: str) -> int:
        
## test part
def titleToNumber(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 36 ms, faster than 55.89% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
"""
def titleToNumber(s):	
	def addSum(digits):
		add_sum = 0
		if digits > 0:
			add_sum = 26**digits + addSum(digits-1)
		return add_sum
	digits = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	add_sum = addSum(len(s)-1) + 1
	for i in range(len(s)):
		add_sum += digits.index(s[-1-i]) * 26 ** i
	return add_sum


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