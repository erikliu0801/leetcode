# ToDo:

"""
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
"""
# Conditions & Concepts
"""
alphanumeric = alph + num
"""
# Code
## submit part
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
## test part
def isPalindrome(s):
	"""
	s: str
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input:"0P"
Output:true
Expected:false

"9;8'4P?X:1Q8`dOfJuJXD6FF,8;`Y4! YBy'Wb:ll;;`;\"JI0c2uvD':!LAk:s\"!'0.!2B55.T1VI?00Du?1,l``RFsc?Y?9vD5 K'3'1b!N8hn:'l. R:9:o`m1r.M2mrJ?`Wjv1`G6i6G`1vjW`?Jrm2M.r1m`o:::R .l':nh8N!b1'3'K 5Dv9?Y?csFR``l,1?uD00?IV1T.55B2!.0'!\"s:kAL!:'Dvu2c0IJ\";`;;ll9bW'yBY !4Y`;8,FF6DXJuJfOd`8Q1:X?P4'8;9"
Output: true
Expected: false

Success
Runtime: 72 ms, faster than 9.41% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.2 MB, less than 94.05% of Python3 online submissions for Valid Palindrome.
"""
def isPalindrome(s):
	s = s.lower()
	s_pure = str()
	alph = [chr(x) for x in range(97,123)]
	alph_num = alph + [str(x) for x in range(0,10)]
	for c in s:
		if c in alph_num:
			s_pure = s_pure + c
	return s_pure == s_pure[::-1]



		

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