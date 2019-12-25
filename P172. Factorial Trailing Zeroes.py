# ToDo:

"""
172. Factorial Trailing Zeroes
Easy

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
## test part
def trailingZeroes(n):
	"""
	n: int
	rtypeL int
	"""
## code here
#1
"""
Time Limit Exceeded
8479
"""
def trailingZeroes(n):
	def factorial(n):
		if n == 1:
			return 1
		else:
			answer = n * factorial(n-1)
		return answer
	if n == 0:
		return 0
	elif n < 0 and n % 2 != 0:
		negative = True
		n = abs(n)
	else:
		negative = False
	factorial_num = factorial(n)
	factorial_num = str(factorial_num)
	num = 0
	for i in range(1,len(factorial_num)):
		if factorial_num[-i] == '0':
			num += 1
		else:
			break
	if negative == True:
		num = 0 - num
	return num

#1.1
"""
how many 5
"""
def trailingZeroes(n):	
	if n < 0 and n % 2 != 0:
		negative = True
	n = abs(n)
	count = 0
	while 5 * count <= n:
		count += 1
	if negative:
		return 1 - count
	else:
		return count - 1

#1.2
"""
Your input:8479
Output:2034
Expected:2116
"""
def trailingZeroes(n):
	negative = False
	if n < 0 and n % 2 != 0:
		negative = True
	n = abs(n)
	if negative == True:
		return 0 - (n//25)*6 - (n%25)//5
	else:
		return (n//25)*6 + (n%25)//5

#1.3
"""
5**i

Success
Runtime: 28 ms, faster than 84.30% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Factorial Trailing Zeroes.
"""
def trailingZeroes(n):
	negative = False
	if n < 0 and n % 2 != 0:
		negative = True
	n = abs(n)
	five_scale = 5
	five_scale_addnum = [1]
	while five_scale < n:
		five_scale *= 5
		five_scale_addnum.append(five_scale_addnum[-1]*5 +1)
	add_num = 0
	for i in range(1,len(five_scale_addnum)+1):
		add_num += (n // five_scale) * five_scale_addnum[-i]
		n %= five_scale
		five_scale //= 5
	if negative == True:
		return 0 - add_num
	else:
		return add_num



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