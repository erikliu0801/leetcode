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

#3 new
def isValid(s):
	if len(s) == 0:
		return True
	if len(s) % 2 != 0:
		return False
	symbol_dict = {"{":"}","(":")","[":"]"}
	while len(s) != 0:
		if symbol_dict[s[0]] == s[1]:
			s = s[2:]
		elif symbol_dict[s[0]] == s[-1]:
			s = s[1:-1]
		else:
			return False
	return True

#3.1
"""
Runtime Error
Last executed input:"(("
"""
def isValid(s):
	symbols = str()
	for c in s:
		if c in ["{","}","(",")","[","]"]:
			symbols += c
	if len(symbols) == 0:
		return True
	if len(symbols) % 2 != 0:
		return False
	symbol_dict = {"{":"}","(":")","[":"]"}
	reversed_symbol_dict = {"}":"{",")":"(","]":"["}
	while len(symbols) != 0:
		if symbol_dict[symbols[0]] == symbols[1]:
			symbols = symbols[2:]
		elif reversed_symbol_dict[symbols[-1]] == symbols[-2]: #KeyError
			symbols = symbols[:-2]
		elif symbol_dict[s[0]] == symbols[-1]:
			symbols = symbols[1:-1]
		else:
			return False
	return True

#4
def isValid(s):
	symbols_left = ["{","(","["]
	symbols_right = ["}",")","]"]
	s_symbols = str()
	for c in s:
		if c in symbols_left or c in symbols_right:
			s_symbols += c
	if len(s_symbols) == 0:
		return True
	if len(s_symbols) % 2 != 0:
		return False
	while len(s_symbols) != 0:
		if symbols_left.index(s_symbols[0]) == symbols_right.index(s_symbols[1]): ## ValueError: not in list
			s_symbols = s_symbols[2:]
		elif symbols_right.index(s_symbols[-1]) == symbols_left.index(s_symbols[-2]):
			s_symbols = s_symbols[:-2]
		elif symbols_left.index(s_symbols[0]) == symbols_right.index(s_symbols[-1]):
			s_symbols = s_symbols[1:-1]
		else:
			return False
	return True

#4.1
def isValid(s):
	symbols_left = ["{","(","["]
	symbols_right = ["}",")","]"]
	s_symbols = str()
	for c in s:
		if c in symbols_left or c in symbols_right:
			s_symbols += c
	if len(s_symbols) == 0:
		return True
	if len(s_symbols) % 2 != 0:
		return False
	while len(s_symbols) != 0:
		if s_symbols[0] in symbols_right:
			return False

		if s_symbols[1] in symbols_right or s_symbols[-1] in symbols_right:
			if symbols_left.index(s_symbols[0]) == symbols_right.index(s_symbols[1]):
				s_symbols = s_symbols[2:]
				continue
			if symbols_left.index(s_symbols[0]) == symbols_right.index(s_symbols[-1]):
				s_symbols = s_symbols[1:-1]
				continue

		if s_symbols[-1] in symbols_right and s_symbols[-2] in symbols_left:
			if symbols_right.index(s_symbols[-1]) == symbols_left.index(s_symbols[-2]):
				s_symbols = s_symbols[:-2]
				continue
		
		return False
	return True

#4.2
"""

"""
def isValid(s):
	symbols_left = ["{","(","["]
	symbols_right = ["}",")","]"]
	s_symbols = str()
	for c in s:
		if c in symbols_left or c in symbols_right:
			s_symbols += c
	if len(s_symbols) == 0:
		return True
	if len(s_symbols) % 2 != 0:
		return False
	while len(s_symbols) != 0:
		if s_symbols[0] not in symbols_left or s_symbols[-1] not in symbols_right:
			return False

		elif s_symbols[-1] == symbols_right[symbols_left.index(s_symbols[0])]:
			s_symbols = s_symbols[1:-1]

		elif s_symbols[1] == symbols_right[symbols_left.index(s_symbols[0])]:
			s_symbols = s_symbols[2:]

		elif s_symbols[-2] == symbols_left[symbols_right.index(s_symbols[-1])]:
			s_symbols = s_symbols[:-2]

		else:
			return False			
	return True

#5
def isValid(s):
	symbols_left = ["{","(","["]
	symbols_right = ["}",")","]"]
	s_symbols = str()
	for c in s:
		if c in symbols_left or c in symbols_right:
			s_symbols += c
	if len(s_symbols) == 0:
		return True
	if len(s_symbols) % 2 != 0:
		return False
	new_len = int()
	while len(s_symbols) != 0:
		if len(s_symbols) == new_len:
			return False
		i = 0
		while i < len(s_symbols)-2:
			if s_symbols[i] in symbols_left:
				if s_symbols[i+1] == symbols_right[symbols_left.index(s_symbols[i])]:
					s_symbols = s_symbols[:i] + s_symbols[i+2:]
				else:
					i += 1
		new_len = len(s_symbols)
	return True



# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_s = ["()", "()[]{}", "(]", "([)]", "{[]}", "[", "]","][]","[]{","(afadfadf)","(([]){})","((","[({(())}[()])]"]
	expected_output = [True, True, False, False, True, False, False, False, False, True, True, False, True]
	for i in range(len(input_s)):
		if isValid(input_s[i]) != expected_output[i]:
			print("Wrong!!! Output:", isValid(input_s[i]))
		else:
			print("Right")
	# print(isValid(input_s[3]))

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