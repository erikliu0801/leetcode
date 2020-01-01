# ToDo:

"""
392. Is Subsequence
Easy
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""
# Conditions & Concepts
"""
len(t) >> len(s)
"""
# Code
## submit part
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
## test part
def isSubsequence(s, t):
	"""
	s: str
	t: str
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input:"acb"
"ahbgdc"
Output:true
Expected:false

Misunderstanding:
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
"""
# def isSubsequence(s, t):
# 	for alphabet in set(s):
# 		if t.count(alphabet) < s.count(alphabet):
# 			return False
# 	return True



#1.1
"""
""
"ahbgdc"

Success
Runtime: 184 ms, faster than 50.28% of Python3 online submissions for Is Subsequence.
Memory Usage: 17.2 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
"""
def isSubsequence(s, t):
	if len(s) == 0:
		return True
	i = 0
	for alphabet in t:
		if alphabet == s[i]:
			i += 1
		if i == len(s):
			break
	return i == len(s)

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