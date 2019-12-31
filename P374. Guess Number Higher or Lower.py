# ToDo:

"""
374. Guess Number Higher or Lower
Easy
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
## test part
def guessNumber(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
"""
adjust from P278 firstBadVersion(n)
def firstBadVersion(n):
	if n in [0,1] or isBadVersion(n) is False:
		return n
	elif isBadVersion(1) is True:
		return 1
	else:
		try_num = n//2
		high_limit, low_limit = n, 1
		while try_num < n:
			if isBadVersion(try_num) is True:
				high_limit = try_num
				try_num = (high_limit + low_limit) // 2
				if high_limit - 1 == low_limit:
					return high_limit
			elif isBadVersion(try_num) is False:
				low_limit = try_num
				try_num = (high_limit + low_limit) // 2
				if low_limit + 1 == high_limit:
					return high_limit

Success
Runtime: 24 ms, faster than 82.42% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower.
Next challenges:
"""
def guessNumber(n):
	if n in [0,1] or guess(n) == 0:
		return n
	elif guess(1) is 0:
		return 1
	else:
		try_num = n//2
		high_limit, low_limit = n, 1
		while try_num < n:
			if guess(try_num) == 0:
				return try_num
			elif guess(try_num) == -1:
				high_limit = try_num
				try_num = (high_limit + low_limit) // 2
				if high_limit - 1 == low_limit:
					return high_limit
			elif guess(try_num) == 1:
				low_limit = try_num
				try_num = (high_limit + low_limit) // 2
				if low_limit + 1 == high_limit:
					return high_limit


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