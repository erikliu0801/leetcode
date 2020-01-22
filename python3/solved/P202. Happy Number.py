# ToDo:

"""
202. Happy Number
Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isHappy(self, n: int) -> bool:
        
## test part
def isHappy(n):
	"""
	n: int
	rtype: bool
	"""
## code here
#1 new
"""
Success
Runtime: 60 ms, faster than 5.78% of Python3 online submissions for Happy Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Happy Number.
"""
def isHappy(n):
	if n < 1:
		return False
	pre = list()
	while n != 1:
		if n in pre:
			return False
		pre.append(n)
		cache = 0
		for c in str(n):
			cache += int(c)**2
		n = cache
	return True



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