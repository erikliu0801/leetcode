# ToDo:

"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
# Concepts


# Code
## submit part
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
## test part
class Solution:
	def lengthOfLongestSubstring(self, s):
## code here
""" Misunderstanding!
#1 build a a-z table and count every times
 
#2 build a a-z been used table and count

#3 sort by a-z then count

#4 dict
   def lengthOfLongestSubstring(self, s):
   	for i in list(s):
   		if list(s)[i] in dict()


#5 String
	def lengthOfLongestSubstring(self, s):
		max_count = 0
		for i, j in enumerate(list(s)):
			if s.count(list(s)[i]) > max_count:
				max_count = s.count(list(s)[i])
		return max_count
"""

#1 List of List of String
"""
whrong Logic 
'dvdf'
"""
	def lengthOfLongestSubstring(self, s):
		unrepeated_substring = []
		string_list = list(s)
		substring = ""
		for i, j in enumerate(string_list):
			if substring.count(j) == 0:
				substring = substring + j
			else:
				unrepeated_substring.append(substring)
				substring = j
		unrepeated_substring.append(substring)
		max_count = 0
		for i, j in enumerate(unrepeated_substring):
			x = len(unrepeated_substring[i])
			if x > max_count:
				max_count = x
		return max_count

#2
	def lengthOfLongestSubstring(self, s):



# Test
## Functional Test
"""
Condition:

"""


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