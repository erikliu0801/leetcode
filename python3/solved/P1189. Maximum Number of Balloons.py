# ToDo:

"""
1189. Maximum Number of Balloons
Easy

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Constraints:

    1 <= text.length <= 10^4
    text consists of lower case English letters only.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
## test part
def maxNumberOfBalloons(text):
	"""
	text: str
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 82.27% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
"""
def maxNumberOfBalloons(text):
	from collections import Counter
	t = Counter("balloon")
	text = Counter(text)
	count = 0
	while text['b'] >= 1 and text['a'] >= 1 and text['l'] >= 2 and text['o'] >= 2 and text['n'] >= 1:
		count += 1
		text.subtract(t)
	return count

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_text = ["nlaebolko", "loonbalxballpoon", "leetcode"]
	expected_output = [1, 2, 0]
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