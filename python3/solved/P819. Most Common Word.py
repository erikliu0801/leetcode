# ToDo:

"""
819. Most Common Word
Easy

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase. 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned. 

Note:
1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
## test part
def mostCommonWord(paragraph, banned):
	"""
	paragraph: str
	banned: List[str]
	rtype: str
	"""
## code here
#1
"""
Wrong Answer
Input: "Bob", []
Output: ""
Expected: "bob"

Success
Runtime: 44 ms, faster than 16.51% of Python3 online submissions for Most Common Word.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Most Common Word.
"""
def mostCommonWord(paragraph, banned):
	from collections import Counter
	alph = [chr(x) for x in range(97, 123)]
	words = []
	word = ''
	for w in paragraph:
		if w.lower() in alph:
			word += w.lower()
		elif word != '':
			words.append(word)
			word = ''
	if word != '':
		words.append(word)
	frequence = Counter(words)
	while frequence:
		frequentest, _ = frequence.most_common(1)[0]
		if frequentest not in banned:
			return frequentest	
		frequence.pop(frequentest)
	return ''

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_paragraph = ["Bob hit a ball, the hit BALL flew far after it was hit.", "Bob"]
	input_banned = [["hit"], []]
	expected_output = ["ball", "bob"]
	for i in range(len(input_paragraph)):
		if mostCommonWord(input_paragraph[i], input_banned[i]) != expected_output[i]:
			print("Wrong!!!")
			print(mostCommonWord(input_paragraph[i], input_banned[i]))
		else:
			print("Right")
	# print(mostCommonWord(input_paragraph[i], input_banned[i]))
	

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