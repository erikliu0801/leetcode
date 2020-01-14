# ToDo:

"""
58. Length of Last Word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
"""
# Concepts 
"""
1. split with ' ' => end with ' '? => string.rstrip()
2. len(last word) => other symbol: re? => no need
3. nothing then return 0
"""
# Code
## submit part
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
## test part
def lengthOfLastWord(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 32 ms, faster than 62.30% of Python3 online submissions for Length of Last Word.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Length of Last Word.
"""
def lengthOfLastWord(s):
	s = s.lstrip()
	s = s.rstrip()
	len_word = 0
	for i in range(len(s)):
		if s[i] == ' ': #end with ' '?
			len_word = 0
		else:
			len_word += 1
	return len_word


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_str = ["Hello World", "Hello World!", "Hello World! ", "Hello World! yes"]
	expected_output = [5, 6, 6, 3]
	for i, j in enumerate(input_str):
		if lengthOfLastWord(input_str[i]) != expected_output[i]:
			print("Wrong!!!")
			print(lengthOfLastWord(input_str[i]))
		else:
			print("Right")		
	# print(lengthOfLastWord(input_str[-1]))
	

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