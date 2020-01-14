# ToDo:

"""
459. Repeated Substring Pattern
Easy
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.


Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

"""
# Conditions & Concepts
"""
lowercase English letters only
0 < len(s) <= 10000

len can be divided by which number e.g. 4 times

"ababcababc"
"ababc" *2

find s.index(s[-1])
slice by s[-1]

#
substring_nums = list()
while s is not NONE:
	substring_nums.apend(s[:s.index(s[-1])])
	s = s[s.index(s[-1])+1:]

"aacbbcaacbbc"
substring_nums = ["aac", "bbc", "aac", "bbc"]

#
substring_i = substring_nums.index(substring_nums[-1]) +1
if substring_i == len(substring_nums) or len(substring_nums) % substring_i != 0:
	return False

for i, substring in enumerate(substring_nums):
	if substring != substring_nums[i % substring_i]:
		return False

return True


"""
# Code
## submit part
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
## test part
def repeatedSubstringPattern(s):
	"""
	s: str
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input: "ababababababaababababababaababababababa"
Output: false
Expected: true
"""
# def repeatedSubstringPattern(s):
# 	substring_nums = list()
# 	while s != str():
# 		substring_nums.append(s[:s.index(s[-1])+1])
# 		s = s[s.index(s[-1])+1:]
# 	substring_i = substring_nums.index(substring_nums[-1]) +1
# 	if substring_i == len(substring_nums) or len(substring_nums) % substring_i != 0:
# 		return False

# 	for i, substring in enumerate(substring_nums):
# 		if substring != substring_nums[i % substring_i]:
# 			return False

# 	return True

#1.1
def repeatedSubstringPattern(s):

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