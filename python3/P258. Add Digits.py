# ToDo:

"""
258. Add Digits
Easy
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Accepted
262.4K
Submissions
475K
Seen this question in a real interview before?

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def addDigits(self, num: int) -> int:
        
## test part
def addDigits(num):
	"""
	num: int
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 20 ms, faster than 99.45% of Python3 online submissions for Add Digits.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Add Digits.
"""
def addDigits(num):
	while num > 9:
		temp = 0
		for j in str(num):
			temp += int(j)
		num = temp
	return num

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