# ToDo:

"""
482. License Key Formatting
Easy
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.

"""
# Conditions & Concepts
"""
lowercase -> uppercase
first group which could be shorter than K, but still must contain at least one character
each group contains exactly K characters

S.upper()
S = S.split("-")
S.reverse()

i = 0
loop:
	if len(S[i]) != K:
		S[i]

S.upper()
S = list(S)[::-1]
key = str()
key_part = str()
for alph in S:
	if len(key_part) < K:
		key_part = alph + key_part
	else:
		key = key_part + '-' + key
		key_part = str()
return key_part + '-' + key[:-1]



"""
# Code
## submit part
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
## test part
def licenseKeyFormatting(S, K):
	"""
	S: str
	K: int
	rtype: str:
	"""
## code here
#1
"""
Input: "r", 1
Output: "R-"
Expected: "R"


Success
Runtime: 96 ms, faster than 23.60% of Python3 online submissions for License Key Formatting.
Memory Usage: 13.5 MB, less than 61.54% of Python3 online submissions for License Key Formatting.
"""
def licenseKeyFormatting(S, K):
	S = list(S.upper())[::-1]
	key = str()
	key_part = str()
	for alph in S:
		if alph != '-':
			if len(key_part) < K:
				key_part = alph + key_part
			else:
				key = key_part + '-' + key
				key_part = alph
	if key_part != str() and key != str():
		return key_part + '-' + key[:-1]
	elif key_part != str() and key == str():
		return key_part
	return key[:-1]

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