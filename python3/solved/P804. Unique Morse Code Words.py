# ToDo:

"""
804. Unique Morse Code Words
Easy

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:

    The length of words will be at most 100.
    Each words[i] will have length in range [1, 12].
    words[i] will only consist of lowercase letters.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
## test part
def uniqueMorseRepresentations(words):
	"""
	words: List[str]
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 32 ms, faster than 76.82% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Morse Code Words.
"""
def uniqueMorseRepresentations(words):
	morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	alph = [chr(x) for x in range(97,123)]
	m_a = {alph[i]:morse[i] for i in range(26)}
	morse_strs = []
	for word in words:
		morse_str = ''
		for w in word.lower():
			morse_str += m_a[w]
		morse_strs.append(morse_str)
	return len(set(morse_strs))


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_words = [["gin", "zen", "gig", "msg"]]
	expected_output = [2]
	for i in range(len(input_words)):
		if uniqueMorseRepresentations(input_words[i]) != expected_output[i]:
			print("Wrong!!!")
			print(uniqueMorseRepresentations(input_words[i]))
		else:
			print("Right")		
	# print(uniqueMorseRepresentations(input_words[-1]))
	

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