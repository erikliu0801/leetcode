# ToDo:

"""
13. Roman to Integer
Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



"""
# Concepts


# Code
## submit part
class Solution:
    def romanToInt(self, s: str) -> int:
## test part

## code here
#1
def romanToInt(s):
	answer = 0
	step = 0
	for i in range(len(s)):
		if step == 1:
			step = 0
			pass
		elif s[i] == 'M' and step != 1:
			answer += 1000
		elif s[i] == 'D' and step != 1:
			answer += 500
		elif s[i] == 'L' and step != 1:
			answer += 50
		elif s[i] == 'V' and step != 1:
			answer += 5
		elif s[i] == 'I' and step != 1:
			answer += 1
		elif i+1 < len(s):
			if s[i] == 'C' and s[i+1] == 'M':
				answer += 900
				step = 1
			elif s[i] == 'C' and s[i+1] == 'D':
				answer += 400
				step = 1
			elif s[i] == 'C' and s[i+1] != 'D' and s[i+1] == 'M':
				answer += 100
				step = 1
			
			elif s[i] == 'X':
				answer += 10
			
			elif s[i] == 'I':
				answer += 1
	return answer

#1.1
"""
"III"
"LVIII"
"""
def romanToInt(s):
	answer = 0
	step = 0
	for i in range(len(s)):
		if step == 1:
			step = 0
			pass
		elif s[i] == 'M' and step != 1:
			answer += 1000
		elif s[i] == 'D' and step != 1:
			answer += 500
		elif s[i] == 'L' and step != 1:
			answer += 50
		elif s[i] == 'V' and step != 1:
			answer += 5
		elif s[i] == 'I' and step != 1:
			answer += 1
		elif i+1 < len(s):
			if s[i] == 'C' 
				if s[i+1] == 'M':
					answer += 900
					step = 1
				elif s[i+1] == 'D':
					answer += 400
					step = 1
				else:
					answer += 100
			
			elif s[i] == 'X':
				if s[i+1] == 'C':
					answer += 90
					step = 1
				elif s[i+1] == 'L':
					answer += 40
					step = 1
				else:
					answer += 10
			
			elif s[i] == 'I':
				if s[i+1] == 'X':
					answer += 9
					step = 1
				elif s[i+1] == 'V':
					answer += 4
					step = 1
				else:
					answer += 1
	return answer
#1.2
"""
"IV", "IX", "MCMXCIV" => ok
Input:"MDLXX"
Output:1560
Expected:1570

Success
Runtime: 44 ms, faster than 89.53% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""
def romanToInt(s):
	answer = 0
	step = 0
	for i in range(len(s)):
		if step == 1:
			step = 0
			pass
		elif s[i] == 'M':
			answer += 1000
		elif s[i] == 'D':
			answer += 500
		elif s[i] == 'L':
			answer += 50
		elif s[i] == 'V':
			answer += 5
		elif i+1 == len(s):
			if s[i] == 'M':
				answer += 1000
			elif s[i] == 'D':
				answer += 500
			elif s[i] == 'C':
				answer += 100
			elif s[i] == 'L':
				answer += 50
			elif s[i] == 'X':
				answer += 10
			elif s[i] == 'V':
				answer += 5
			elif s[i] == 'I':
				answer += 1
		elif i+1 < len(s):
			if s[i] == 'C':
				if s[i+1] == 'M':
					answer += 900
					step = 1
				elif s[i+1] == 'D':
					answer += 400
					step = 1
				else:
					answer += 100
			
			elif s[i] == 'X':
				if s[i+1] == 'C':
					answer += 90
					step = 1
				elif s[i+1] == 'L':
					answer += 40
					step = 1
				else:
					answer += 10
			
			elif s[i] == 'I':
				if s[i+1] == 'X':
					answer += 9
					step = 1
				elif s[i+1] == 'V':
					answer += 4
					step = 1
				else:
					answer += 1
	return answer

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MDLXX"]
	expected_output = [3, 4, 9, 58, 1994, 1570]
	for i, j in enumerate(input):
		if romanToInt(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(romanToInt(input[i]))
		else:
			print("Right")

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