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
		s1 = s[:i] + s[i+1:]
		if s1 == s1[::-1]: return True
	return False

#1.1
def validPalindrome(s):
	if s == s[::-1]: return True
	middle = len(s)//2
	left = s[:middle]
	right = s[middle:]


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