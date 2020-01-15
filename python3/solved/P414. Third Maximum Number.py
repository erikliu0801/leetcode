# ToDo:

"""
414. Third Maximum Number
Easy

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
## test part
def thirdMax(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
def thirdMax(nums):
	x = set(nums)
	for _ in range(2):
		if len(x) >=1 :
			x -= max(x)
		else:
			return max(nums)
	if len(x) >= 1:
		return max(x)

#1.1
"""
Success
Runtime: 52 ms, faster than 83.44% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.2 MB, less than 23.08% of Python3 online submissions for Third Maximum Number.
"""
def thirdMax(nums):
	x = set(nums)
	i = 0
	while len(x) >= 1 and i != 2:
		x.remove(max(x))
		i += 1
	if len(x) >= 1:
		return max(x)
	return max(nums)

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