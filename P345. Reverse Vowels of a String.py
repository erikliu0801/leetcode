# ToDo:

"""
345. Reverse Vowels of a String
Easy
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reverseVowels(self, s: str) -> str:
        
## test part
def reverseVowels(s):
	"""
	s: str
	rtype: str
	"""
## code here
#1
"""
Input: "aA"
Output: "aA"
Expected: "Aa"

Success
Runtime: 60 ms, faster than 57.27% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 14 MB, less than 93.33% of Python3 online submissions for Reverse Vowels of a String.
"""
def reverseVowels(s):
	s = list(s)
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	vowels_nums = list()
	for i, alphabet in enumerate(s):
		if alphabet in vowels:
			vowels_nums.append(alphabet)
			s[i] = 'vowel'
	s1 = ''
	for alphabet in s:
		if alphabet == 'vowel':
			s1 += vowels_nums[-1]
			vowels_nums.pop()
		else:
			s1 += alphabet
	return s1






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