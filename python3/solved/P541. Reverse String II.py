# ToDo:

"""
541. Reverse String II
Easy

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
## test part
def reverseStr(s, k):
	"""
	s: str
	k: int
	rtype: str
	"""
## code here
#1
def reverseStr(s, k):
	reversed_str = ''
	n = 0
	while len(s) > k*(n+1):
		reverse_part = slice(k*n,k*(n+1),-1) #?
		original_part = slice(k*(n+1),k*(n+2))
		reversed_str += s[reverse_part]
		reversed_str += s[original_part]
		n += 2
	return reversed_str

#1.1
"""
reverse_s = s[k*n:k*(n+1):-1] #can NOT work

Success
Runtime: 24 ms, faster than 93.31% of Python3 online submissions for Reverse String II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse String II.
"""
def reverseStr(s, k):
	if k == 1 or s == '':
		return s
	reversed_str = ''
	n = 0
	while len(s) > k*n:
		reverse_s = s[k*n:k*(n+1)][::-1]
		original_s = s[k*(n+1):k*(n+2)]
		reversed_str += reverse_s + original_s
		n += 2
	return reversed_str

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