# ToDo:

"""
830. Positions of Large Groups
Easy

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        
## test part
def largeGroupPositions(S):
	"""
	S: str
	rtype: List[List[int]]
	"""
## code here
#1
"""
Wrong Answer
Input: "aaa"
Output: []
Expected: [[0,2]]

Success
Runtime: 32 ms, faster than 90.66% of Python3 online submissions for Positions of Large Groups.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Positions of Large Groups.
"""
def largeGroupPositions(S):
	now = ''
	first_p = 0
	count = 0
	position_nums = []
	for i, c in enumerate(S):
		if c != now:
			#record
			if count >= 3: position_nums.append([first_p,i-1])
			#reset
			now = c
			count = 1
			first_p = i
		else: count += 1
	if count >= 3: position_nums.append([first_p,i])
	return position_nums


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_S = ["abbxxxxzzy", "abc", "abcdddeeeeaabbbcd", "aaa"]
	expected_output = [[[3,6]], [], [[3,5],[6,9],[12,14]], [[0,2]]]
	for i in range(len(input_S)):
		if largeGroupPositions(input_S[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', largeGroupPositions(input_S[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(largeGroupPositions(input_S[-1]))
	

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