# ToDo:

"""
344. Reverse String
Easy
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
## test part
def reverseString(s):
	"""
	s: List[str])
	rtype: None
	"""
## code here
#1
"""
Success
Runtime: 208 ms, faster than 92.43% of Python3 online submissions for Reverse String.
Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Reverse String.
"""
def reverseString(s):
	# s = s[::-1]
	s.reverse()

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