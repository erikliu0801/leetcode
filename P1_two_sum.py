```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```
nums1 = [2, 7, 11, 15]
nums2 = [3,2,4]
target = 9

# test part
def twoSum(nums, target):
	for i, element in enumerate(nums):
		for _last_i, last_element in enumerate(nums[i+1:]):
			last_i = _last_i + i + 1
			if element+last_element == target:
				print([element, last_element])
				print([i, last_i]) #[0,1]


def twoSum(nums, target):
	for i, element in enumerate(nums):
		for _last_i, last_element in enumerate(nums[i+1:]):
			last_i = _last_i + i + 1
			if element+last_element == target:
				return [i, last_i] 


#1 OK -> Status:Wrong_Answer nums2 = [3,2,4], target = 6 -> 1.1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	for i, element in enumerate(nums):
    		for last_i, last_element in enumerate(nums[i:]):
    			if element+last_element == target:
    				# return [element, last_element] #[2,7]
    				return [i, last_i] #[0,1]


#1.1 OK -> Status:Time_Limit_Exceeded -> 1,2
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i, element in enumerate(nums):
			for _last_i, last_element in enumerate(nums[i+1:]):
				last_i = _last_i + i + 1
				if element+last_element == target:
					return [i, last_i] 

#1.2 
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]: