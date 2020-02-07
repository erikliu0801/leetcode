# ToDo:

"""
696. Count Binary Substrings
Easy

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.

"""
# Conditions & Concepts
"""
number of non-empty (contiguous) substrings that have the same number of 0's and 1's

Hint: How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?

"000111" : 3
"11100" : 2
"00011100": 3 + 2 = 5
"""
# Code
## submit part
class Solution:
	def countBinarySubstrings(self, s: str) -> int:
		
## test part
def countBinarySubstrings(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 240 ms, faster than 23.45% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 13.1 MB, less than 91.67% of Python3 online submissions for Count Binary Substrings.
"""
def countBinarySubstrings(s):
	if len(set(s)) == 1:
		return 0
	count = 0
	zeros = 0
	ones = 0
	for i, b in enumerate(s):
		if b == '0':
			if (i != 0 and s[i-1] == '1'):
				count += min(zeros, ones)
				zeros = 1
			else:
				zeros += 1
		else:
			if (i != 0 and s[i-1] == '0'):
				count += min(zeros, ones)
				ones = 1
			else:
				ones += 1
	return count+min(zerosn, ones)

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = ["00110011", "10101", "00011100"]
	expected_output = [6, 4, 5]
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