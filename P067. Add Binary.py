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
a: 1 or 0
b: 1 or 0
carry: 1 or 0
events: 2**3 = 8
results: 4

results	| events
---------------
(num, carry) | (a, b, carry)
---------------
(1, 1) | (1,1,1)
(0, 1) | (1,1,0) (1,0,1) (0,1,1)
(1, 0) | (1,0,0) (0,1,0) (0,0,1)
(0, 0) | (0,0,0)
================
results	| events
---------------
(num, carry) | (a, carry)
---------------
(0, 1) | (1,1)
(1, 0) | (1,0) (0,1)
(0, 0) | (0,0)
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
"""
'str' object does not support item assignment
"""
# def addBinary(a, b):
# 	position = 1
# 	carry = False
# 	if len(a) < len(b):
# 		a, b = b, a
# 	while position <= len(b):
# 		if a[0-position] == '1' and b[0-position] == '1':
# 			if carry==False:
# 				a[0-position] = '1'
# 			else: #carry==True
# 				a[0-position] = '0'
# 			carry = True			
# 			position += 1
# 		else:
# 			carry = False
# 			a[0-position] = '1'
# 			position += 1

# 	while carry == True:
# 		if position != len(a):
# 			if a[0-position] == '1':
# 				a[0-position] = '0'
# 				carry = True			
# 				position += 1
# 			else:
# 				a[0-position] = '0'
# 				carry = False
# 		else:
# 			a = '1'+a
# 			carry = False
# 	return a

#1.1
def addBinary(a, b):
	position = 1
	carry = False
	bi_sum = ''
	if len(a) < len(b):
		a, b = b, a
	while position <= len(b):
		if a[0-position] == '1' and b[0-position] == '1':
			if carry==True:
				bi_sum = '1' + bi_sum
			else: #carry==False
				bi_sum = '0'  + bi_sum
			carry = True			
			position += 1
		else:			
			if a[0-position] == '1' or b[0-position] == '1' and carry == False:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = False
			position += 1

	while carry == True:
		if position <= len(a):
			if a[0-position] == '1':
				bi_sum = '0' + bi_sum
				carry = True			
				position += 1
			else:
				bi_sum = '0' + bi_sum
				carry = False
		else:
			bi_sum = '1' + bi_sum
			carry = False


	return bi_sum

#1.2
def addBinary(a, b):
	position = 1
	carry = False
	bi_sum = ''
	if len(a) < len(b):
		a, b = b, a
	while position <= len(b):
		if a[0-position] == '1' and b[0-position] == '1':
			if carry == True:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = True
			position +=1
		elif a[0-position] == '0' and b[0-position] == '0':
			if carry == True:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = False
			position +=1
		else:
			if carry == True:
				bi_sum = '0' + bi_sum
			else:
				bi_sum = '1' + bi_sum
			position +=1
	while carry == True:
		if position <= len(a):
			if a[0-position] == '1':
				bi_sum = '0' + bi_sum
				carry = True
				position +=1
			else:
				bi_sum = '0' + bi_sum
				carry = False			
		else:
			bi_sum = '1' + bi_sum
			carry = False
	return bi_sum

#1.3
"""
Input:"101111","10"
Output:"1000001"
Expected:"110001"

Success
Runtime: 28 ms, faster than 94.00% of Python3 online submissions for Add Binary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Binary.
"""
def addBinary(a, b):
	position = 1
	carry = False
	bi_sum = ''
	if len(a) < len(b):
		a, b = b, a
	while position <= len(b):
		if a[0-position] == '1' and b[0-position] == '1':
			if carry == True:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = True
			position +=1
		elif a[0-position] == '0' and b[0-position] == '0':
			if carry == True:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = False
			position +=1
		else:
			if carry == True:
				bi_sum = '0' + bi_sum
			else:
				bi_sum = '1' + bi_sum
			position +=1
	while carry == True:
		if position <= len(a):
			if a[0-position] == '1':
				bi_sum = '0' + bi_sum
				carry = True
			else:
				bi_sum = '1' + bi_sum
				carry = False			
		else:
			bi_sum = '1' + bi_sum
			carry = False
		position +=1
	if position <= len(a):
		bi_sum = a[:1-position] + bi_sum
	return bi_sum

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_str_a = ["11", "1010", "100", "101111"]
	input_str_b = ["1", "1011", "110010", "10"]
	expected_output = ["100", "10101", "110110", "110001"]
	for i in range(len(input_str_a)):
		if addBinary(input_str_a[i], input_str_b[i]) != expected_output[i]:
			print("Wrong!!!")
			print(addBinary(input_str_a[i], input_str_b[i]))
		else:
			print("Right")
	# print(addBinary(input_str_a[-1], input_str_b[-1]))
	

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