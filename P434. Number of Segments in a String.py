# ToDo:

"""
434. Number of Segments in a String
Easy

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def countSegments(self, s: str) -> int:
        
## test part
def countSegments(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input: ", , , ,        a, eaefa"
Output: 13
Expected: 6

Input: ",, , ,        a, eaefa"
Expected: 5
- continuous space
"""
def countSegments(s):
	s = s.strip()
	if s == str():
		return 0
	return len(s.split(' '))

#1.1
def countSegments(s):
	length = 0
	alph = [chr(a) for a in range(65,91)] + [chr(a) for a in range(97,123)]
	word = False
	for p in s:
		if p in [',',';']:
			length += 1
		elif word == False and p in alph:
			word = True
		elif word == True and p == ' ':
			word = False
			length += 1



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