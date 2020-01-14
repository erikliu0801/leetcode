# ToDo:

"""
520. Detect Capital
Easy

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

 

Example 1:

Input: "USA"
Output: True 

Example 2:

Input: "FlaG"
Output: False

 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
## test part
def detectCapitalUse(word):
	"""
	word: str
	rtype: bool
	"""
## code here
#1
"""
return not word.islower() #""

return not word.isupper() #"Flag"

Success
Runtime: 28 ms, faster than 68.92% of Python3 online submissions for Detect Capital.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Detect Capital.
"""
def detectCapitalUse(word):
	if word.isupper() == True:
		return True
	word = word[1:]
	return word == word.lower()




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