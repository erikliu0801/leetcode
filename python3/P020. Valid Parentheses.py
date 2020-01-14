# ToDo:
# to be continued
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
	if len(symbol_list)%2 != 0:
		answer = False
	else:
		for i, j in enumerate(symbol_list):
			if j == '(': j1 =')'
			elif j == '{': j1 ='}'
			elif  j == '[': j1 =']'	

			if j in '({[':
				if i+1 == len(symbol_list):
					answer = False
					break
				elif j1 != symbol_list[-1-i] and j1 != symbol_list[i+1]:
					answer = False
					break
	return answer

#1.1
def isValid(s):
	answer = True
	symbol_list = list(s)
	if len(symbol_list)%2 != 0:
		answer = False
	else:
		for i, j in enumerate(symbol_list):
			if j == '(': j1 =')'
			elif j == '{': j1 ='}'
			elif  j == '[': j1 =']'	

			if j in '({[':
				if i+1 == len(symbol_list):
					answer = False
					break
				elif j1 != symbol_list[-1-i] and j1 != symbol_list[i+1]:
					answer = False
					break
	return answer

#1.2
"""
"(([]){})"
True
"""
def isValid(s):
	answer = True
	symbol_list = list(s)
	if len(symbol_list)%2 != 0:
		answer = False
	else:
		for i, j in enumerate(symbol_list):
			if j == '(': j1 =')'
			elif j == '{': j1 ='}'
			elif  j == '[': j1 =']'	

			if j in '({[':
				if i+1 == len(symbol_list):
					answer = False
					break
				elif j1 != symbol_list[-1-i] and j1 != symbol_list[i+1]:
					answer = False
					break
	for j in symbol_list:
		if j not in '(){}[]':
			answer = False
	return answer

#1.3
def isValid(s):
	answer = True
	symbol_list = list(s)
	if len(symbol_list)%2 != 0:
		answer = False
	else:
		for i, j in enumerate(symbol_list):
			if j == '(': j1 =')'
			elif j == '{': j1 ='}'
			elif  j == '[': j1 =']'	

			if j in '({[':
				if i+1 == len(symbol_list):
					answer = False
					break
				elif j1 != symbol_list[-1-i] and j1 != symbol_list[i+1]:
					answer = False
					break
				elif j1 == symbol_list[-1-i]:
					symbol_list = symbol_list[i+1:-i]
				elif j1 == symbol_list[i+1]:
					symbol_list = symbol_list[i+2:]
	for j in symbol_list:
		if j not in '(){}[]':
			answer = False
	return answer

#1.4
def isValid(s):
	answer = True
	symbol_list = list(s)
	if len(symbol_list)%2 != 0:
		answer = False
	else:
		for i, j in enumerate(symbol_list):
			if j == '(': j1 =')'
			elif j == '{': j1 ='}'
			elif  j == '[': j1 =']'	

			if j in '({[':
				if i+1 == len(symbol_list):
					answer = False
					break
				elif j1 != symbol_list[-1-i] and j1 != symbol_list[i+1]:
					answer = False
					break
				elif j1 == symbol_list[-1-i]:
					symbol_list = symbol_list[i+1:-i]
				elif j1 == symbol_list[i+1]:
					symbol_list = symbol_list[i+2:]
	for j in symbol_list:
		if j not in '(){}[]':
			answer = False
	return answer

#2
"""
1. []
2. [...]
"""
def isValid(s):
	answer = True
	symbol_list = list(s)
	if len(symbol_list)%2 != 0:
		answer = False
	else:
		#1
		for i, j in enumerate(symbol_list):
			if j == '(' and symbol_list[i+1] == ')':
				symbol_list = symbol_list[i+2:]
			elif j == '{' and symbol_list[i+1] == '}':
				symbol_list = symbol_list[i+2:]
			elif  j == '[' and symbol_list[i+1] == ']':
				symbol_list = symbol_list[i+2:]
		#2
		for i, j in enumerate(symbol_list):
			if j == '(': j1 =')'
			elif j == '{': j1 ='}'
			elif  j == '[': j1 =']'	

			if j in '({[':
				if i+1 == len(symbol_list):
					answer = False
					break
				elif j1 != symbol_list[-1-i] and j1 != symbol_list[i+1]:
					answer = False
					break
				elif j1 == symbol_list[-1-i]:
					symbol_list = symbol_list[i+1:-i]
				elif j1 == symbol_list[i+1]:
					symbol_list = symbol_list[i+2:]

	for j in symbol_list:
		if j not in '(){}[]':
			answer = False
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