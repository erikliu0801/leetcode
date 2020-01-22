# ToDo:

"""
205. Isomorphic Strings
Easy
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
## test part
def isIsomorphic(s, t):
	"""
	s: str
	t: str
	rtype: bool
	"""
## code here
#1
"""
Input: "abba", "abab"
Output: true
Expected :false
"""

def isIsomorphic(s, t):
	if len(s) != len(t):
		return False
	else:
		for i in range(len(s)):
			if s.count(s[i]) != t.count(t[i]):
				return False
		return True

#2 new
"""
Success
Runtime: 36 ms, faster than 76.87% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Isomorphic Strings.
"""
def isIsomorphic(s, t):
	if len(s) != len(t) or len(set(s)) != len(set(t)):
		return False
	else:
		s_to_t = dict()
		for i in range(len(s)):
			if s[i] in s_to_t:
				if s_to_t[s[i]] != t[i]:
					return False
			else:
				s_to_t[s[i]] = t[i]
		return True

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_s = ['egg', 'foo', 'paper', 'abba']
	input_t = ['add', 'bar', 'title', 'abab']
	expected_output = [True, False, True, False]
	for i in range(len(input_s)):
		if isIsomorphic(input_s[i],input_t[i]) != expected_output[i]:
			print("Wrong!!!")
			print(isIsomorphic(input_s[i],input_t[i]))
		else:
			print("Right")		
	# print(isIsomorphic(input_s[-1],input_t[-1]))
	

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