# ToDo:

"""
290. Word Pattern
Easy
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
## test part
def wordPattern(pattern, str):
	"""
	pattern: str
	str: str
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 77.71% of Python3 online submissions for Word Pattern.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Pattern.
"""
def wordPattern(pattern, str):
	nums_str = str.split(' ')
	if len(pattern) != len(nums_str):
		return False
	p_to_s = {}
	have_ds = set()
	for dp, ds in zip(pattern, nums_str):
		if dp not in p_to_s:
			if ds in have_ds:
				return False
			p_to_s[dp] = ds
			have_ds.add(ds)
		if p_to_s[dp] != ds:
			return False
	return True

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_pattern = ["abba", "abba", "abba", "abba"]
	input_str = ["dog cat cat dog", "dog cat cat fish", "dog cat cat dog", "dog dog dog dog"]
	expected_output = [True, False, False, False]
	for i in range(len(input_pattern)):
		if wordPattern(input_pattern[i], input_str[i]) != expected_output[i]:
			print("Wrong!!!")
			print(wordPattern(input_pattern[i], input_str[i]))
		else:
			print("Right")		
	# print(wordPattern(input_pattern[-1], input_str[-1]))
	

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