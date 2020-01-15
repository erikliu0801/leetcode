# ToDo:

"""
476. Number Complement
Easy
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

"""
# Conditions & Concepts
"""
num  = list(str(bin(5))[2:])
comlement = str()
for i, j in enumerate(num):
	if j == '1':
		comlement = comlement + '0'
	else:
		comlement = comlement + '1'
return int(complement,2)


"""
# Code
## submit part
class Solution:
    def findComplement(self, num: int) -> int:
        
## test part
def findComplement(num):
	"""
	num: int
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 55.70% of Python3 online submissions for Number Complement.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number Complement.
"""
def findComplement(num):
	num  = list(str(bin(num))[2:])
	complement = str()
	for j in num:
		if j == '1':
			complement = complement + '0'
		else:
			complement = complement + '1'
	return int(complement,2)


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