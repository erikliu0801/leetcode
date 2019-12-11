# ToDo:

"""
7. Reverse Integer: Math
Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


"""
# Concepts
"""
1. x>=0 or x<0
2. recursive
"""

# Code
## submit part
class Solution:
    def reverse(self, x: int) -> int:


## test part

## code here
#1
"""
Wrong Answer
Playground Debug
Input:1534236469
Output:9646324351
Expected:0
=> 32-bit signed integer
"""
def reverse(x):
	#
	negative = False
	if x < 0:
		x = -x
		negative = True
	#
	reverse_str = []
	for i in range(len(str(x))):
		reverse_str.append(str(x)[-1-i])
	revers_x = ''
	for j in reverse_str:
		revers_x = revers_x + j
	revers_x = int(revers_x)
	if negative==True:
		revers_x = 0 - revers_x
	return revers_x
#1.1
"""
Wrong Answer
Input:900000
Output:0
Expected:9
"""
def reverse(x):
	if x<-231 or x>230:
		return 0
	else:
		#
		negative = False
		if x < 0:
			x = -x
			negative = True
		#
		reverse_str = []
		for i in range(len(str(x))):
			reverse_str.append(str(x)[-1-i])
		revers_x = ''
		for j in reverse_str:
			revers_x = revers_x + j
		revers_x = int(revers_x)
		if negative==True:
			revers_x = 0 - revers_x
		return revers_x

#1.2
"""
Wrong Answer
Input:1463847412
Output:0
Expected:2147483641

Success
Runtime: 36 ms, faster than 63.39% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
"""
def reverse(x):
	#
	negative = False
	if x < 0:
		x = -x
		negative = True
	#
	reverse_str = []
	for i in range(len(str(x))):
		reverse_str.append(str(x)[-1-i])
	revers_x = ''
	for j in reverse_str:
		revers_x = revers_x + j
	revers_x = int(revers_x)
	if negative==True:
		revers_x = 0 - revers_x
	if revers_x<-2**31 or revers_x>2**31-1:
		revers_x = 0
	return revers_x

# Test
## Functional Test
"""
Condition:

"""


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