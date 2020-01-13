# ToDo:

"""
496. Next Greater Element I
Easy

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:

    All elements in nums1 and nums2 are unique.
    The length of both nums1 and nums2 would not exceed 1000.


"""
# Conditions & Concepts
"""
nums1 belongs to nums2
nums2.sort()



"""
# Code
## submit part
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
## test part
def nextGreaterElement(nums1, nums2):
	"""
	nums1: List[int]
	nums2: List[int]
	rtype: List[int]
	"""
## code here
#1
"""
Wrong Answer
Input: [1,3,5,2,4], [6,5,4,3,2,1,7]
Output: [7,-1,-1,-1,-1]
Expected: [7,7,7,7,7]

"""
# def nextGreaterElement(nums1, nums2):
# 	nums2.sort()
# 	for i, num in enumerate(nums1):
# 		if nums2.index(num) == len(nums2) -2:
# 			nums1[i] = -1
# 		else:
# 			nums1[i] = nums2[nums2.index(num)+1]
# 	return nums1

#1.1
"""
Success
Runtime: 84 ms, faster than 18.93% of Python3 online submissions for Next Greater Element I.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.
"""
def nextGreaterElement(nums1, nums2):
	for i, num in enumerate(nums1):
		nums2_temp = nums2[nums2.index(num)+1:]
		if nums2_temp == list():
			nums1[i] = -1
		else:
			for num2 in nums2_temp:
				if num2 > num:
					nums1[i] = num2
					break
			if nums1[i] == num:
				nums1[i] = -1
	return nums1


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums1 = [[4,1,2], [2,4], [1,3,5,2,4]]
	input_nums2 = [[1,3,4,2], [1,2,3,4], [6,5,4,3,2,1,7]]
	expected_output = [[-1,3,-1], [3,-1], [7,7,7,7,7]]
	for i in range(len(input_nums1)):
		if nextGreaterElement(input_nums1[i], input_nums2[i]) != expected_output[i]:
			print("Wrong!!!")
			print(nextGreaterElement(input_nums1[i], input_nums2[i]))
		else:
			print("Right")		
	# print(nextGreaterElement(input_nums1[-1], input_nums2[-1]))
	

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