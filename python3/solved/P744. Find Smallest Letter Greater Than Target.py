# ToDo:

"""
744. Find Smallest Letter Greater Than Target
Easy

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Note:

letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
## test part
def nextGreatestLetter(letters, target):
	"""
	letters: List[str]
	target: str
	rtype: str
	"""
## code here
#1
"""
Success
Runtime: 116 ms, faster than 46.17% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Find Smallest Letter Greater Than Target.
"""
def nextGreatestLetter(letters, target):
	t_num = ord(target)
	l_nums = [ord(c) for c in letters]
	l_nums.sort()
	for num in l_nums:
		if num > t_num: return chr(num)
	return chr(l_nums[0])

#1.1
"""
Success
Runtime: 120 ms, faster than 29.31% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Smallest Letter Greater Than Target.
"""
def nextGreatestLetter(letters, target):
	t_num = ord(target)
	close_num = float('inf')
	smallest_num = float('inf')
	for c in letters:
		c_num = ord(c)
		if c_num > t_num and c_num < close_num:
			close_num = c_num
		if c_num < smallest_num:
			smallest_num = c_num
	if close_num != float('inf'):
		return chr(close_num)
	return chr(smallest_num)


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_letters = [["c", "f", "j"],["c", "f", "j"],["c", "f", "j"],["c", "f", "j"],["c", "f", "j"],["c", "f", "j"]]
	inpurt_target = ["a", "c", "d", "g", "j", "k"]
	expected_output = ["c", "f", "f", "j", "c", "c"]
	for i in range(len(input_letters)):
		if nextGreatestLetter(input_letters[i], inpurt_target[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', nextGreatestLetter(input_letters[i], inpurt_target[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(nextGreatestLetter(input_letters[-1], inpurt_target[-1]))
	

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