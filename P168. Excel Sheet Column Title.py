# ToDo:

"""
168. Excel Sheet Column Title
Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

	1 -> A
	2 -> B
	3 -> C
	...
	26 -> Z
	27 -> AA
	28 -> AB 
	...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def convertToTitle(self, n: int) -> str:
		
## test part
def convertToTitle(n):
	"""
	n: int
	rtype: str
	"""
## code here
#1
# def addSum(digits):
# 		add_sum = 0
# 		if digits > 0:
# 			add_sum = 26**digits + addSum(digits-1)
# 		return add_sum

#1.1
"""
len(digits_num) = 1 => ok

"""
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		digits_sum = 26
		digits_num = [26]
		while digits_sum < n:
			digits_sum += digits_sum*26
			digits_num.append(digits_sum)
		digits_num.pop()
		all_digits = ''
		while len(digits_num) != 0:
			all_digits = all_digits + digits[n % digits_num[-1]-1]
			digits_num.pop()
		return all_digits

#1.2
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	
		digits_sum, digits_num, digits_level =0, 1, 1
		while digits_num <= n and digits_sum != n:
			digits_num *= 26
			digits_level += 1
			digits_sum += digits_num
		digits_num //= 26
		digits_level -= 1
		all_digits = ''
		while digits_level != 0:
			all_digits = all_digits + digits[n//digits_num-1]
			n %= 26
			digits_num //= 26
			digits_level -= 1
		return all_digits

#1.3
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	
		digits_sum, digits_num, digits_level =0, 1, 1
		while digits_num <= n:
			digits_num *= 26
			digits_level += 1
			digits_sum += digits_num
		digits_num //= 26
		digits_level -= 1
		all_digits = ''
		while digits_level != 0:
			all_digits = all_digits + digits[n//digits_num-1]
			n %= 26
			digits_num //= 26
			digits_level -= 1
		return all_digits

#1.4
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	
		digits_sum, digits_num, digits_level = 0, 1, 0
		while digits_sum < n:
			digits_num *= 26
			digits_level += 1
			digits_sum += digits_num		
		if digits_sum == n:
			return 'Z' * digits_level
		else:
			all_digits = ''
			while  digits_level != 0:
				all_digits = all_digits + digits[n//26**digits_level]
				n -= 26**digits_level
				digits_level -= 1
			return all_digits


#1.5
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']	
		digits_sum, digits_num, digits_level = 0, 1, 0
		while digits_sum < n:
			digits_num *= 26
			digits_level += 1
			digits_sum += digits_num
		if digits_sum == n:
			return 'Z' * digits_level
		else:
			all_digits = ''
			while n != -1:
				all_digits = digits[n % 26] + all_digits
				n = n//26
				if n == 27:
					n -= 1
			return all_digits

#1.6
"""
Success
Runtime: 28 ms, faster than 78.28% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
"""
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']	
		digits_sum, digits_num, digits_level = 0, 1, 0
		while digits_sum < n:
			digits_num *= 26
			digits_level += 1
			digits_sum += digits_num
		if digits_sum == n:
			return 'Z' * digits_level
		else:
			all_digits = ''
			while digits_level > 0:
				all_digits = digits[n % 26] + all_digits
				if n % 26 == 0:
					n = n//26 -1
				else:
					n = n//26
				digits_level -= 1
			return all_digits


# Test
## Functional Test
"""
# Conditions & Concepts

"""

if __name__ == '__main__':
	input_int = [1, 26, 28, 701, 702, 703, 17576, 18278, 18279]
	expected_output = ['A', 'Z', 'AB', 'ZY', 'ZZ', 'AAA', 'YYZ', 'ZZZ', 'AAAA']
	for i in range(len(input_int)):
		if convertToTitle(input_int[i]) != expected_output[i]:
			print("Wrong!!!")
			print(convertToTitle(input_int[i]))
		else:
			print("Right")		
	# print(convertToTitle(input_int[-1]))
	

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