# ToDo:

"""
1170. Compare Strings by Frequency of the Smallest Character
Easy

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

 

Constraints:

    1 <= queries.length <= 2000
    1 <= words.length <= 2000
    1 <= queries[i].length, words[i].length <= 10
    queries[i][j], words[i][j] are English lowercase letters.



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
## test part
def numSmallerByFrequency(queries, words):
	"""
	queries: List[str]
	words: List[str]
	rtype: List[int]
	"""
## code here
#1
def numSmallerByFrequency(queries, words):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_queries = [["cbd"], ["bbb","cc"]]
	input_words = [["zaaaz"], ["a","aa","aaa","aaaa"]]
	expected_output = [[1], [1,2]]
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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