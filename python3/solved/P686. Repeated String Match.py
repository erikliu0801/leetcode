# ToDo:

"""
686. Repeated String Match
Easy

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
# Conditions & Concepts
"""
A = "abcd"
B = "cd abcd ab"
"""
# Code
## submit part
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
## test part
def repeatedStringMatch(A, B):
	"""
	A: str
	B: str
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input:"abc", "cabcabca"
Output: -1
Expected: 4

Success
Runtime: 28 ms, faster than 96.73% of Python3 online submissions for Repeated String Match.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Repeated String Match.
"""
def repeatedStringMatch(A, B):
	if B in A:
		return 1
	if set(B) != set(A):
		return -1
	times = len(B) // len(A)
	top = times + 2
	while times <= top:
		if B in A * times:
			return times
		times += 1
	return -1

#1.1


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_A = ["abcd", "c", "abc"]
	input_B = ["cdabcdab", "", "cabcabca"]
	expected_output = [3, 1, 4]
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