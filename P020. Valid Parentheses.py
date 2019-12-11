# ToDo:

"""
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

"""
# Concepts


# Code
## submit part
class Solution:
    def isValid(self, s: str) -> bool:
## test part

## code here
#1
def isValid(s):

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = []
	expected_output = []
	for i, j in enumerate(input):
		if isValid(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(isValid(input[i]))
		else:
			print("Right")		
	# print(isValid(input[-1]))

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