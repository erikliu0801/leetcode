# ToDo:

"""
925. Long Pressed Name
Easy

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character. 

Note:

    name.length <= 1000
    typed.length <= 1000
    The characters of name and typed are lowercase letters.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
## test part
def isLongPressedName(name, typed):
	"""
	name: str
	typed: str
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input: "kikcxmvzi", "kiikcxxmmvvzz"
Output: true
Expected: false

Success
Runtime: 32 ms, faster than 43.29% of Python3 online submissions for Long Pressed Name.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Long Pressed Name.
"""
def isLongPressedName(name, typed):
	if name == typed: return True
	if set(name) != set(typed): return False
	last = ''
	j = 0
	for i, nc in enumerate(name):
		while j < len(typed):
			if typed[j] == nc:
				j += 1
				break
			elif typed[j] == last:
				j += 1
			else : return False
		if i < len(name) and j == len(typed) and typed[j-1] != nc: return False #
		last = nc
	rest = set(typed[j:])
	if rest:
		if len(rest) > 1 : return False
		return True if last in rest else False
	return True

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_name = ["alex", "saeed", "leelee", "laiden", "kikcxmvzi", "izi"]
	input_typed = ["aaleex", "ssaaedd", "lleeelee", "laiden", "kiikcxxmmvvzz", "izz"]
	expected_output = [True, False, True, True, False, False]
	for i in range(len(input_name)):
		if isLongPressedName(input_name[i], input_typed[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', isLongPressedName(input_name[i], input_typed[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	print(isLongPressedName(input_name[-1], input_typed[-1]))
	

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