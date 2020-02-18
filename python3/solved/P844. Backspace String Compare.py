# ToDo:

"""
844. Backspace String Compare
Easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:
    Can you solve it in O(N) time and O(1) space?
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
## test part
def backspaceCompare(S, T):
	"""
	S: str
	T: str
	rtype: bool
	"""

## code here
#1
# def backspaceCompare(S, T):
# 	if S == T: return True
# 	S = S[::-1]
# 	i = 0
# 	i_del = 0
# 	T = T[::-1]
# 	j = 0
# 	j_del = 0
# 	while i < len(S) and j < len(T):
# 		while S[i] == '#':
# 			i += 1
# 			i_del += 1
# 		while T[j] == '#':
# 			j += 1
# 			j_del += 1
# 		while i_del > 0:
# 			i += 1
# 			i_del -= 1
# 		while j_del > 0:
# 			j += 1
# 			j_del -= 1
# 		if S[i] != T[j]: 
# 			return False
# 		else:
# 			i += 1
# 			j += 1
# 	if i == len(S) and j == len(T): return True
# 	if (set(S[i:]) | set(T[j:])) != set('#'):
# 		return False
# 	return True

#1.1
# def backspaceCompare(S, T):
# 	def helper(S, i):
# 		i_del = 0
# 		while S[i] == '#':
# 			i += 1
# 			i_del += 1
# 		while i_del > 0:
# 			i += 1
# 			i_del -= 1
# 		return i

# 	if S == T: return True
# 	S = S[::-1]
# 	i = helper(S,0)
# 	T = T[::-1]
# 	j = helper(T,0)
# 	while i < len(S) and j < len(T):
# 		if S[i] != T[j]: 
# 			return False
# 		i = helper(S,i+1)
# 		j = helper(T,j+1)
# 	if i == len(S) and j == len(T): return True
# 	if (set(S[i:]) | set(T[j:])) != set('#'):
# 		return False
# 	return True

#1.2
"""
Success
Runtime: 16 ms, faster than 99.73% of Python3 online submissions for Backspace String Compare.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
"""
def backspaceCompare(S, T):
	def helper(M):
		res = ''
		cd = 0
		for c in M[::-1]:
			if c == '#':
				cd += 1				
			elif cd > 0:
				cd -= 1
			else:
				res = c + res
		return res
	return helper(S) == helper(T)

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_S = ["ab#c", "ab##", "a##c", "a#c"]
	input_T = ["ad#c", "c#d#", "#a#c", "b"]
	expected_output = [True, True, True, False]
	for i in range(len(input_S)):
		if backspaceCompare(input_S[i], input_T[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', backspaceCompare(input_S[i], input_T[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(backspaceCompare(input_S[-1], input_T[-1]))
	

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