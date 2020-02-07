# ToDo:

"""
680. Valid Palindrome II
Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
## test part
def validPalindrome(s):
	"""
	s: str
	rtype: bool
	"""
## code here
#1
"""
Time Limit Exceeded
"""
def validPalindrome(s):
	if s == s[::-1]: return True
	for i in range(len(s)):
		#if s[i] == s[-1-i]: continue
		s1 = s[:i] + s[i+1:]
		if s1 == s1[::-1]: return True
	return False

#1.2
"""
Success
Runtime: 80 ms, faster than 91.35% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 13.3 MB, less than 56.25% of Python3 online submissions for Valid Palindrome II.
"""
def validPalindrome(s):
	if s == s[::-1]: return True
	i = 0
	while i <= len(s)//2:
		if s[i] != s[-1-i]:
			s1 = s[:i] + s[i+1:]
			s2 = s[:-1-i] + s[len(s)-i:]
			return s1 == s1[::-1] or s2 == s2[::-1]
		i += 1

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_s = ["abccba","dabccba","abccbad","dabcdfcba"]
	expected_output = [True, True, True, False]
	for i in range(len(input_s)):
		if validPalindrome(input_s[i]) != expected_output[i]:
			print("Wrong!!!")
			print(validPalindrome(input_s[i]))
		else:
			print("Right")
	# print(validPalindrome(input_s[-1]))
	

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