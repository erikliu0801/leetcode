# ToDo:

"""
551. Student Attendance Record I
Easy
You are given a string representing an attendance record for a student. The record only contains the following three characters:

    'A' : Absent.
    'L' : Late.
    'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

Input: "PPALLP"
Output: True

Example 2:

Input: "PPALLL"
Output: False


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def checkRecord(self, s: str) -> bool:
        
## test part
def checkRecord(s):
	"""
	s: str
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input: "LALL"
Output: false
Expected: true

more than two CONTINUOUS 'L' (late)
"""
def checkRecord(s):
	return s.count('A') < 2 and s.count('L') < 3

#1.1
"""
Success
Runtime: 24 ms, faster than 88.61% of Python3 online submissions for Student Attendance Record I.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Student Attendance Record I.
"""
def checkRecord(s):
	return s.count('A') < 2 and 'LLL' not in s


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