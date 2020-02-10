# ToDo:

"""
859. Buddy Strings
Easy

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Note:
    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist only of lowercase letters.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
## test part
def buddyStrings(A, B):
	"""
	A: str
	B: str
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 86.61% of Python3 online submissions for Buddy Strings.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Buddy Strings.
"""
def buddyStrings(A, B):
	if set(A) != set(B) or len(A) < 2 or len(B) < 2:
		return False
	if A == B :
		from collections import Counter
		a = Counter(A)
		if a.most_common(1)[0][1] >=2:
			return True
		return False
	a_b = None
	for a, b in zip(A, B):
		if a != b:
			if a_b:
				if a != a_b[1] or b != a_b[0]:
					return False
			a_b = (a,b)
	if a_b:
		return True
	else:
		return False
	

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_A = ["ab", "ab", "aa", "aaaaaaabc", ""]
	input_B = ["ba", "ab", 'aa', "aaaaaaacb", "aa"]
	expected_output = [True, False, True, True, False]
	for i in range(len(input_A)):
		if buddyStrings(input_A[i], input_B[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', buddyStrings(input_A[i], input_B[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(buddyStrings(input_A[-1], input_B[-1]))
	

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