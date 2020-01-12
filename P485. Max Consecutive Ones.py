# ToDo:

"""
485. Max Consecutive Ones
Easy
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""
# Conditions & Concepts
"""
consecutive_nums = list()
while nums.count(0)!=0:
	i = nums.inex(0)
	consecutive_nums.append(i)
	if i != len(nums)+1:
		nums = nums[i+1:]
	else:
		break
return max(consecutive_nums)


"""
# Code
## submit part
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
## test part
def findMaxConsecutiveOnes(nums):
	"""
	nums: List[int]
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input: [0,1]
Output: 0
Expected: 1

Time Limit Exceeded
[1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1]
Runtime: 576 ms
"""
def findMaxConsecutiveOnes(nums):
	if nums.count(0) == 0:
		return len(nums)
	elif nums.count(1) == 0:
		return 0
	consecutive_nums = list()
	while nums.count(0)!=0:
		i = nums.index(0)
		consecutive_nums.append(i)
		if i != len(nums)+1:
			nums = nums[i+1:]
		else:
			break
	if nums != list():
		consecutive_nums.append(len(nums))
	return max(consecutive_nums)

#1.1
"""
Runtime: 584 ms
"""
def findMaxConsecutiveOnes(nums):
	if nums.count(0) == 0:
		return len(nums)
	elif nums.count(1) == 0:
		return 0
	max_consecutive_num = 0
	while nums.count(0)!=0:
		i = nums.index(0)
		if i > max_consecutive_num:
			max_consecutive_num = i
		if i != len(nums)+1:
			nums = nums[i+1:]
		else:
			break
	if nums != list():
		if i > max_consecutive_num:
			max_consecutive_num = len(nums)
	return max_consecutive_num

#1.2
"""
Runtime: 84 ms

Wrong Answer
Input: [1]
Output: 0
Expected: 1


Success
Runtime: 412 ms, faster than 14.95% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones.
"""
def findMaxConsecutiveOnes(nums):
	max_count = 0
	count = 0 
	for i in nums:
		if i == 0:
			if count > max_count:
				max_count = count
			count = 0
		else:
			count += 1
	if count != 0 and count > max_count:
		max_count = count
	return max_count


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