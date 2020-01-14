# ToDo:

"""
500. Keyboard Row
Easy

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""
# Conditions & Concepts
"""
row1 = ['q','w','e','r','t','y','u','i','o','p']
row2 = ['a','s','d','f','g','h','j','k','l']
row3 = ['z','x','c','v','b','n','m']
"""
# Code
## submit part
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
## test part
def findWords(words):
	"""
	words: List[str]
	rtype: List[str]
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 56.58% of Python3 online submissions for Keyboard Row.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Keyboard Row.
"""
def findWords(words):
	row1 = set(['q','w','e','r','t','y','u','i','o','p'])
	row2 = set(['a','s','d','f','g','h','j','k','l'])
	row3 = set(['z','x','c','v','b','n','m'])
	for word in words.copy():
		word_tmp = set(word.lower())
		# if word_tmp not in row1 and word_tmp not in row2 and word_tmp not in row3:
		if word_tmp.issubset(row1) or word_tmp.issubset(row2) or word_tmp.issubset(row3):
			continue
		else:
			words.remove(word)
	return words


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