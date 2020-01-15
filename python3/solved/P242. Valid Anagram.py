# ToDo:

"""
242. Valid Anagram
Easy
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
## test part
def isAnagram(s,t):
	"""
	s: str
	t: str
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Valid Anagram.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
"""
def isAnagram(s,t):
	if set(s) != set(t):
		return False
	for alphabet in set(s):
		if s.count(alphabet) != t.count(alphabet):
			return False
	return True

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