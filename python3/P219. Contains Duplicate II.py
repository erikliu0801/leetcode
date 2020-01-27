# ToDo:

"""
219. Contains Duplicate II
Easy
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
## test part
def containsNearbyDuplicate(nums, k):
	"""
	nums: List[int]
	k: int
	rtype: bool
	"""
## code here
#1
"""
Misunderstanding
"""
def containsNearbyDuplicate(nums, k):
	if len(nums) < 2 or len(set(nums)) == 1:
		return k == 0
	if nums[0] != nums[-1]:
		return k == len(nums) -1
	i, j = 0, len(nums)-1
	while nums[i] == nums[0]:
		i += 1
	while nums[j] == nums[-1]:
		j -= 1
	return k == j-i+2

#2
"""
Input: [99,99] 2
Output: false
Expected: true
"""
def containsNearbyDuplicate(nums, k):
	if len(set(nums)) == len(nums):
		return False
	c = list()
	c_i_j = list()
	for m, num in enumerate(nums):
		if num in c:
			c_i_j[c.index(num)].append(m)
		else:
			c.append(num)
			c_i_j.append([m])
	k_s = set()
	for m in c_i_j:
		for n, i in enumerate(m):
			for j in m[n+1:]:
				k_s.add(abs(j-i))
	return k in k_s


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[1,2,3,1], [1,0,1,1], [1,0,1,1], [1,0,1,1], [1,2,3,1,2,3], [1,2,3,1,2,3], [99,99]]
	input_k = [3, 1, 2, 3, 2, 3, 2]
	expected_output = [True, True, True, True, False, True, False]
	for i in range(len(input_nums)):
		if containsNearbyDuplicate(input_nums[i], input_k[i]) != expected_output[i]:
			print("Wrong!!!")
			print(containsNearbyDuplicate(input_nums[i], input_k[i]))
		else:
			print("Right")		
	# print(containsNearbyDuplicate(input_nums[-1], input_k[-1]))
	

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