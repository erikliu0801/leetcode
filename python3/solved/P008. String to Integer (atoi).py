# ToDo:

"""
8. String to Integer (atoi)
Medium

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2**31) is returned.



"""
# Concepts

# discard ' '
# +/-
# if not ' ' or int -> 0
# over 32-bit -> -2147483648 or 2147483647
# output : int

# Code
## submit part
class Solution:
    def myAtoi(self, str: str) -> int:
## test part

## code here
#1
"""
Input:"+1"
Output:0
Expected:1 => ok

Input:"-+1"
Output:1
Expected:0 =>

Input:"   +0 123"
Output:123
Expected:0


Input:"-   234"
Output:-234
Expected:0

Input:"0-1"
Output:-1
Expected:0
"""
def myAtoi(str):
	negative = False
	nums = 0
	pre_answer = ''
	for i, j in enumerate(str):
		if j == ' ' and pre_answer == '' and nums==0:
			pass
		elif j == '-' or j == '+' and pre_answer == '':
			if j == '-' and nums == 0:
				negative = True
				nums += 1
			elif j == '+' and nums == 0:
				negative = False
				nums += 1
			else:
				pre_answer = '0'
				break
		elif j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '0':
			pre_answer = pre_answer + j
		else:
			if pre_answer == '':
				pre_answer = '0'
			break
	if pre_answer == '':
		pre_answer = '0'
	if negative == False:
		answer = int(pre_answer)
	else: 
		answer = 0 - int(pre_answer)
	if answer<-2**31 or answer>2**31-1:
		if answer < -2**31:
			answer = -2147483648
		else:
			answer = 2147483647
	return answer

#1.1
"""
Runtime: 32 ms, faster than 88.29% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).
"""
def myAtoi(str):
	negative = False
	nums = 0
	pre_answer = ''
	for i, j in enumerate(str):
		if j == ' ' and pre_answer == '' and nums==0:
			pass
		elif j == '-' and pre_answer == '' and nums == 0:
			negative = True
			nums += 1
		elif j == '+' and pre_answer == '' and nums == 0:
			nums += 1
		elif j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '0':
			pre_answer = pre_answer + j
		else:
			if pre_answer == '':
				pre_answer = '0'
			break
	if pre_answer == '':
		pre_answer = '0'
	if negative == False:
		answer = int(pre_answer)
	else: 
		answer = 0 - int(pre_answer)
	if answer<-2**31 or answer>2**31-1:
		if answer < -2**31:
			answer = -2147483648
		else:
			answer = 2147483647
	return answer


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = ['42','   -42', '4193 with words', 'words and 987', '-91283472332', '+1','+-2', '--1', '-+1', '   +0 123', '-   234' ,'0-1']
	expected_output = [42, -42, 4193, 0, -2147483648, 1, 0, 0 ,0, 0, 0, 0]
	for i, j in enumerate(input):
		if myAtoi(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(myAtoi(input[i]))
		else:
			print("Right")
	# print(myAtoi(input[2]))

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