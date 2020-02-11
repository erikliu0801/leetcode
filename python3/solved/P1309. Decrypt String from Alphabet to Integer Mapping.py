# ToDo:

"""
1309. Decrypt String from Alphabet to Integer Mapping
Easy

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 

Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:

Input: s = "1326#"
Output: "acz"

Example 3:

Input: s = "25#"
Output: "y"

Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"

 

Constraints:

    1 <= s.length <= 1000
    s[i] only contains digits letters ('0'-'9') and '#' letter.
    s will be valid string such that mapping is always possible.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def freqAlphabets(self, s: str) -> str:
        
## test part
def freqAlphabets(s):
	"""
	s: str
	rtype: str
	"""
## code here
#1
"""
Success
Details
Runtime: 28 ms, faster than 73.19% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
"""
def freqAlphabets(s):
	#string = [str(x) for x in range(10)]
	#string.extend([str(x)+'#' for x in range(10,27)])
	low = [chr(x) for x in range(97,123)]
	cd = 0
	decrypt_s = ''
	for i in range(len(s)):
		if cd > 0:
			cd -= 1
			continue
		if s[-1-i] == '#':
			index = int(s[-3-i:-1-i]) -1
			cd = 2
		else:
			index = int(s[-1-i])-1
		decrypt_s = low[index] + decrypt_s
	return decrypt_s







# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_s = ["10#11#12", "1326#", "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"]
	expected_output = ["jkab", "acz", "y"]
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