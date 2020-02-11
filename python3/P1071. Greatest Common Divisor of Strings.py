# ToDo:

"""
1071. Greatest Common Divisor of Strings
Easy

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Note:

    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] and str2[i] are English uppercase letters.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
## test part
def gcdOfStrings(str1, str2):
	"""
	str1: str
	str2: str
	rtype: str
	"""
## code here
#1
def gcdOfStrings(str1, str2):
	if set(str1) != set(str2) or (len(str1) * len(str2)) == 0 : return ""
	common = ""
	for c in str2:
		


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = ["ABCABC", "ABABAB", "LEET"]
	input2 = ["ABC", "ABAB", "CODE"]
	expected_output = ["ABC", "AB", ""]
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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