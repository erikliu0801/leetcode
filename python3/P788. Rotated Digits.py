# ToDo:

"""
788. Rotated Digits
Easy

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
N  will be in range [1, 10000].
"""
# Conditions & Concepts
"""
useful : 0, 1, 8
mainly : 2, 5, 6, 9


10: 2, 5, 6, 9
20: 2, 5, 6, 9, 12, 15, 16, 19, 20
30: 2, 5, 6, 9, 12, 15, 16, 19, 20, 21, 22, 25, 26, 28, 29
40: 2, 5, 6, 9, 12, 15, 16, 19, 20, 21, 22, 25, 26, 28, 29

"""
# Code
## submit part
class Solution:
    def rotatedDigits(self, N: int) -> int:
        
## test part
def rotatedDigits(N):
	"""
	N: int
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input: 857
Output: 343
Expected: 247

hundred_digit e.g. 200,201,...,299

"""
def rotatedDigits(N):
	nums = [None, None, True, False, False, True, True, False, None, True]
	g_nums = [    2,5,6,   9]
	u_nums = [0,1,       8]
	count = 0 
	import math
	while N > 10:
		digit = int(math.log10(N))
		n = N // (10 ** digit)



	return count + len([x for x in good_nums if x <= N])

#1.1
def rotatedDigits(N):
	#nums = [None, None, True, False, False, True, True, False, None, True]
	nums = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_N = [10000, 5000, 2500, 1250, 1000, 625, 300, 150, 100, 90, 80, 70, 60 , 50, 40, 30, 20, 10]
	expected_output = [2320, 976, 780, 418, 316, 196, 129, 56, 40, 34, 29, 29, 23, 16, 15, 15, 9, 4]
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