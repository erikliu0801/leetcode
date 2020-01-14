# ToDo:

"""
28. Implement strStr()
Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


"""
# Concepts


# Code
## submit part
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
## test part
def strStr(haystack, needle):
	"""
	haystack: str
	needle: str
	rtype: int
	"""

## code here
#1
"""
Success
Runtime: 28 ms, faster than 90.78% of Python3 online submissions for Implement strStr().
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement strStr().
"""
def strStr(haystack, needle):
	if needle not in haystack:
		return -1
	elif needle == "":
		return 0
	else:
		answer = -1
		for i in range(len(haystack)):
			if haystack[i] == needle[0]:
				count = 0
				for l in range(len(needle)):
					if haystack[i+l] == needle[l]:
						count += 1
				if count == len(needle):
					answer = i
					break
		if answer != -1:
			return answer
		else:
			return -1


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_haystack = ["hello", "aaaaa", "aaaaa","helloll","heLLoll","a"]
	input_needle = ["ll", "bba", "","ll","ll","a"]
	expected_output = [2, -1, 0, 2, 5, 0]
	for i, j in enumerate(input_haystack):
		if strStr(input_haystack[i], input_needle[i]) != expected_output[i]:
			print("Wrong!!!")
			print(strStr(input_haystack[i], input_needle[i]))
		else:
			print("Right")		
	# print(strStr(input_haystack[-1], input_needle[-1]))
	

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