# ToDo:

"""
58. Length of Last Word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5


"""
# Concepts


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
def lengthOfLastWord(s):

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_str = []
	expected_output = []
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