# ToDo:

"""
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""
# Concepts
# out of '(', ')', '{', '}', '[' and ']'
# e.g. []{}
# e.g. {[]}

# Code
## submit part
class Solution:
    def isValid(self, s: str) -> bool:
## test part

## code here
#1
def isValid(s):
	answer = True
	list_s = list(s)
	symbol_list = []
	for j in list_s:
		if j in '(){}[]':
			symbol_list.append(j)
	for i, j in enumerate(symbol_list):
		if j == '(': j1 =')'
		elif j == '{': j1 ='}'
		elif  j == '[': j1 =']'

		if j1!=symbol_list[-1-i]:
			answer = False
			break
	return answer





# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = ["()", "()[]{}", "(]", "([)]", "{[]}"]
	expected_output = [true, false, true, false, true]
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