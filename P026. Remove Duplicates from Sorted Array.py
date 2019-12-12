# ToDo:

"""
26. Remove Duplicates from Sorted Array
Easy

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""
# Concepts
# modify original Array
# return length of modified Array

# Code
## submit part
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
## test part

## code here
#1
"""
[1,1,1,1]
"""
def removeDuplicates(nums):
	for j in nums:
		if nums.count(j) > 1:
			nums.remove(j)
	return len(nums)

#1.1
"""
Input
[-50,-50,-50,-49,-49,-48,-46,-46,-46,-46,-45,-45,-45,-45,-44,-44,-44,-43,-43,-43,-43,-43,-43,-43,-42,-41,-41,-40,-40,-39,-38,-38,-38,-38,-38,-38,-36,-35,-34,-33,-32,-31,-31,-30,-29,-28,-27,-26,-26,-26,-25,-22,-21,-21,-21,-21,-20,-20,-19,-18,-17,-17,-17,-17,-17,-17,-17,-16,-16,-14,-13,-12,-11,-11,-11,-10,-9,-7,-7,-7,-5,-5,-5,-4,-4,-4,-3,-3,-3,-2,-2,-1,-1,-1,-1,0,1,1,1,2,2,3,3,5,6,6,7,8,8,10,10,10,11,11,11,14,14,17,17,17,18,18,18,19,20,21,21,23,23,23,23,24,24,24,24,24,25,27,27,27,28,29,30,30,31,32,33,34,35,36,37,37,37,37,37,38,38,38,39,39,41,41,41,41,44,44,45,45,46,46,46,46,46,47,47,47,47,48,48,50,50]
Output
[-50,-49,-48,-46,-45,-44,
-43,
-43,-42,-41,-40,-39,-38,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-22,-21,-20,-19,-18,-17,-16,-14,-13,-12,-11,-10,-9,-7,-5,-4,-3,-2,-1,0,1,2,3,5,6,7,8,10,11,14,17,18,19,20,21,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,45,46,47,48,50]
Expected
[-50,-49,-48,-46,-45,-44,-43,-42,-41,-40,-39,-38,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-22,-21,-20,-19,-18,-17,-16,-14,-13,-12,-11,-10,-9,-7,-5,-4,-3,-2,-1,0,1,2,3,5,6,7,8,10,11,14,17,18,19,20,21,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,45,46,47,48,50]
"""
def removeDuplicates(nums):
	for j in nums:
		if nums.count(j) > 1:
			nums.remove(j)
	for j in nums:
		if nums.count(j) > 1:
			nums.remove(j)
	return len(nums)

#1.2
"""
160 / 161 test cases passed.
Status: Time Limit Exceeded
"""
def removeDuplicates(nums):
	for j in nums:
		if nums.count(j) > 1:
			nums.remove(j)
	for j in nums:
		if nums.count(j) > 1:
			nums.remove(j)
	for j in nums:
		if nums.count(j) > 1:
			nums.remove(j)
	return len(nums)

#1.3
def removeDuplicates(nums):
	j1 = nums[0]
	count = 0
	for i, j in enumerate(nums):
		if j1 == j:
			count += 1
		else:
			nums[i+count]

	return len(nums)


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = []
	expected_output = []
	for i, j in enumerate(input):
		if func(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input[i]))
		else:
			print("Right")		
	# print(removeDuplicates(input1[-1]))
	

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