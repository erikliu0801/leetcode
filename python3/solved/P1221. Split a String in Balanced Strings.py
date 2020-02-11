# ToDo:

"""
1221. Split a String in Balanced Strings
Easy

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

 

Constraints:

    1 <= s.length <= 1000
    s[i] = 'L' or 'R'



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
## test part
def balancedStringSplit(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 44 ms, faster than 8.75% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
"""
def balancedStringSplit(s):
	count_R = 0
	count_L = 0
	count_balanced_sub = 0
	for c in s:
		if c == 'R':
			count_R += 1
		else: #c == 'L'
			count_L += 1
		if count_L == count_R:
			count_balanced_sub += 1
			count_R = 0
			count_L = 0
	return count_balanced_sub




# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_s = []
	expected_output = []
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