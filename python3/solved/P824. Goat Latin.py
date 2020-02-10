# ToDo:

"""
824. Goat Latin
Easy

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:
1. If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
2. If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
3. Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin. 

Notes:
S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def toGoatLatin(self, S: str) -> str:
		
## test part
def toGoatLatin(self, S: str) -> str:
	"""
	S: str
	rtype: str
	"""
## code here
#1
"""
Wrong Answer
Input: "HZ sg L"
Output: "ZHmaa gsmaaa "
Expected : "ZHmaa gsmaaa Lmaaaa"

Success
Runtime: 28 ms, faster than 66.33% of Python3 online submissions for Goat Latin.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Goat Latin.
"""
def toGoatLatin(S):
	word = ''
	w_end = ''
	transed_S = ''
	index = 1
	vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
	up = set([chr(x) for x in range(65,91)])
	low = set([chr(x) for x in range(97,123)])
	for c in (S+' '):
		if word == '' and w_end == '':
			if c in vowel:
				word = c
			if c in ((up | low) - vowel):
				w_end = c
		elif c in (up | low):
			word += c
		else:
			if word != '' or w_end != '':
				transed_S += word + w_end + 'ma' + ('a' * index)
				index += 1
				word, w_end = '', ''
			transed_S += c
	return transed_S[:-1]

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_S = ["I speak Goat Latin", "The quick brown fox jumped over the lazy dog", "HZ sg L"]
	expected_output = ["Imaa peaksmaaa oatGmaaaa atinLmaaaaa", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa", "ZHmaa gsmaaa Lmaaaa"]
	for i in range(len(input_S)):
		if toGoatLatin(input_S[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', toGoatLatin(input_S[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(toGoatLatin(input_S[-1]))
	

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