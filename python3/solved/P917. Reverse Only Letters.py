# ToDo:

"""
917. Reverse Only Letters
Easy

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Note:

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122 
    S doesn't contain \ or "

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        
        
## test part
def reverseOnlyLetters(S):
	"""
	S: str
	rtype: str
	"""
## code here
#1
"""
Success
Runtime: 36 ms, faster than 16.38% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Only Letters.
"""
def reverseOnlyLetters(S):
	i_c = {}
	up = set([chr(x) for x in range(65,91)])
	low = set([chr(x) for x in range(97,123)])
	reversed_nums = list()
	for i, c in enumerate(S):
		if c in (up | low):
			reversed_nums.append(c)
		else:
			i_c[i] = c
	reversed_nums.reverse()
	for i in i_c:
		reversed_nums.insert(i, i_c[i])
	reversed_S = ''
	for c in reversed_nums : reversed_S += c
	return reversed_S


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_S = ["ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!"]
	expected_output = ["dc-ba", "j-Ih-gfE-dCba", "Qedo1ct-eeLg=ntse-T!"]
	for i in range(len(input_S)):
		if reverseOnlyLetters(input_S[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', reverseOnlyLetters(input_S[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(reverseOnlyLetters(input_S[-1]))
	

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