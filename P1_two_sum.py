# ToDo:
# 1. Optimize to S1.2
# 2. FT debug
# 3. UT 

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# Code
## test part
nums1 = [2, 7, 11, 15]
nums2 = [3,2,4]
target = 9

def twoSum(nums, target):
	for i, element in enumerate(nums):
		for _last_i, last_element in enumerate(nums[i+1:]):
			last_i = _last_i + i + 1
			if element+last_element == target:
				# return [i, last_i]
				return i, last_i


## 1 Status:Wrong_Answer nums2 = [3,2,4], target = 6 -> 1.1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	for i, element in enumerate(nums):
    		for last_i, last_element in enumerate(nums[i:]):
    			if element+last_element == target:
    				# return [element, last_element] #[2,7]
    				return [i, last_i] #[0,1]


## 1.1 Status:Time_Limit_Exceeded -> 1,2
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i, element in enumerate(nums):
			for _last_i, last_element in enumerate(nums[i+1:]):
				last_i = _last_i + i + 1
				if element+last_element == target:
					return [i, last_i] 

## 1.2 
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:

# Test
## Functional Test
"""
Condition:
	len(list):3~10
	randon1, randon2 in len(list)
	target = list[randon1]+list[randon2] 
"""
def twoSum_test(twoSum,maxLen:int,maxRange:int,times:int):
	right_answer = 0
	wrong_answer = 0
	for _ in range(maxRange):
		import random
		random.randint(1,max)
		nums_test =[]
		tlen =random.randint(1,maxLen)
		for i in range(tlen):
			nums_test.append(random.randint(1,max)) #Disorder
		first_num = random.randint(0,tlen-1)
		second_num = random.randint(0,tlen-1)
		while first_num > second_num or first_num == second_num:
			second_num = random.randint(0,tlen-1)
		target_num = nums_test[first_num] + nums_test[second_num]
		target_list = [first_num,second_num]
		twoSum(nums_test,target_num) #probably bug
		if i != first_num or last_i != second_num:
			wrong_answer += 1
		else:
			right_answer += 1

		# test
		import time
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		return right_answer
		return wrong_answer
	print("wrong answer=",wrong_answer)
	print("right answer=",right_answer)

$twoSum_test(twoSum, 20 , 200, 10)

## Performance Test
import cProfile
cProfile.run('twoSum([2, 7, 11, 15],9)')


## Unit Test
import unittest
class Test(unittest.TestCase):
	def test(self):
		pass