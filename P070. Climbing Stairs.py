# ToDo:

"""
70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def climbStairs(self, n: int) -> int:
## test part
def climbStairs(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
def climbStairs(n):
	if n in [1,2,3]:
		return n
	elif n > 3:
		steps = 0
		for i in range((n//2)+1):
			two = i
			one = n - i * 2
			if one > two:
				a ,b = one +1 , two
			else:
				b, a = one ,two +1
			if a == 0 or b ==0:
				steps += 1
			else:
				numerator = 1
				denominator = 1
				for i in range(b):
					numerator *= a - i
					denominator *= 1 +i
				steps += numerator//denominator
		return steps
	else:
		return 0

#2 
"""
func C
"""
def mathCombination(a,b):
	if a in [0] or b in [0]:
		return 1
	if b > a:
		a, b = b, a
	numerator = 1
	denominator = 1
	for i in range(b):
		numerator *= a - i
		denominator *= 1 +i
	return numerator//denominator
#2.1
"""
Success
Runtime: 20 ms, faster than 98.72% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
"""
def climbStairs(n):
	def mathCombination(a,b):
		if a in [0] or b in [0]:
			return 1
		if b > a:
			a, b = b, a
		numerator = 1
		denominator = 1
		for i in range(b):
			numerator *= a - i
			denominator *= 1 +i
		return numerator//denominator
	if n in [1,2,3]:
		return n
	elif n > 3:
		two, steps = 0, 0		
		while n >= 0:
			steps += mathCombination(n+two, two)
			n += -2
			two += 1
		return steps
	else:
		return 0






# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_int = [1, 2, 3, 4, 5, 6, 7, 8, 25]
	expected_output = [1, 2, 3, 5, 8, 13 ,21, 34, 121393]
	for i in range(len(input_int)):
		if climbStairs(input_int[i]) != expected_output[i]:
			print("Wrong!!!")
			print(climbStairs(input_int[i]))
		else:
			print("Right")
	# print(climbStairs(input_int[5]))
	

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