# ToDo:

"""
409. Longest Palindrome
Easy
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
## test part
def longestPalindrome(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 24 ms, faster than 97.93% of Python3 online submissions for Longest Palindrome.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.
"""
def longestPalindrome(s):
	count_nums = list()
	for alphabet in set(s):
		count_nums.append(s.count(alphabet))
	longest_palindrome = 0
	for i, num in enumerate(count_nums):
		if num//2 >= 1:
			longest_palindrome += num - num%2
			count_nums[i] = num%2
	if 1 in count_nums:
		longest_palindrome += 1
	return longest_palindrome

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