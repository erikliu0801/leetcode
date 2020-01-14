# ToDo:

"""
507. Perfect Number
Easy

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:

Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8) 
"""
# Conditions & Concepts
"""
divisors = [1, num]
divisor
"""
# Code
## submit part
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
## test part
def checkPerfectNumber(num):
	"""
	num: int
	rtype: bool:
	"""
## code here
#1
"""
Runtime Error
Last executed input: -6

Success
Runtime: 32 ms, faster than 79.27% of Python3 online submissions for Perfect Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Perfect Number.
"""
def checkPerfectNumber(num):
	if num <= 0:
		return False
	divisors = set([1])
	import math
	divisor = int(math.sqrt(num))
	while divisor != 1:
		if num%divisor == 0:
			divisors.add(divisor)
			divisors.add(num//divisor)
		divisor -= 1
	divisors.discard(num)
	return num == sum(divisors)

#2
def checkPerfectNumber(num):
	# return num in [6,28,496,8128] ... 33550336

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = [6,28,496,8128]
	expected_output = [True, True, True, True]
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