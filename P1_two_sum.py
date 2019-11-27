```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```
nums = [2, 7, 11, 15]
target = 9

#1 OK
class Solution:
    def twoSum(self, nums, target):
    	for i, element in enumerate(nums):
    		for last_element in nums[i:]:
    			if element+last_element == target:
    				return [element, last_element]

#2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	i=0
    	for element in nums:
    		nums[i]