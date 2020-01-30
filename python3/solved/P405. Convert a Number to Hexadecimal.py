# ToDo:

"""
405. Convert a Number to Hexadecimal
Easy

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

"""
# Conditions & Concepts
"""
two’s complement: 
hex(4,294,967,295) = "ffffffff"
-4,294,967,296 = - 2**32 < 32-bit < 2**32 -1 = 4,294,967,296 - 1

"""
# Code
## submit part
class Solution:
    def toHex(self, num: int) -> str:
        
## test part
def toHex(num):
	"""
	num: int
	rtype: str
	"""
## code here
#1
"""
Success
Runtime: 16 ms, faster than 99.01% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Convert a Number to Hexadecimal.
"""
def toHex(num):
	if num >= 0:
		return hex(num)[2:]
	if num < 0:
		return hex(4294967296+num)[2:]

#2
"""
Success
Runtime: 32 ms, faster than 16.63% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Convert a Number to Hexadecimal.
"""
def toHex(num):
	if num == 0:
		return "0"
	if num < 0:
		num += 4294967296
	import math
	hex_list = [str(x) for x in range(10)]
	hex_list.extend([chr(x) for x in range(97,103)])
	power = int(math.log(num,16))
	hex_num = ""
	while power >= 0:
		hex_num += hex_list[num // (16 ** power)]
		num %= (16 ** power)
		power -= 1
	return hex_num

	

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_num = [16, 26,0, -1,-2, -16]
	expected_output = ["10", "1a","0", "ffffffff", "fffffffe", "fffffff0"]
	for i in range(len(input_num)):
		if toHex(input_num[i]) != expected_output[i]:
			print("Wrong!!!")
			print(toHex(input_num[i]))
		else:
			print("Right")		
	# print(toHex(input_num[-1]))
	

## Performance Test
import cProfile
cProfile.run('')
15*16**8+

## Unit Test
import unittest
class Test(unittest.TestCase):
	def test(self):
		pass

if __name__ == '__main__':
    unittest.main()