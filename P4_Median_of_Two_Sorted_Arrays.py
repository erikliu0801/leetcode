# ToDo:

"""
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
# Concepts
# 1. check ether len(nums1) and len(nums2) even
# 2. len(list), list[0], list[-1]

# Code
## submit part
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
## test part

## code here
#1 assume len(nums1, nums2) isPrime
	def findMedianSortedArrays(self, nums1, nums2):
		mid1, mid2 = len(nums1)//2, len(nums2)//2
		answer = 0
		while answer == 0:
			if nums1[mid1] > nums2[mid2]:
				# nums1 to left
				mid1 = mid1//2
				# nums2 to right
				mid2 = mid2*3//2
			elif nums1[mid1] < nums2[mid2]:
				# nums2 to left
				mid2 = mid2 // 2
				# nums1 to right
				mid1 = mid1 * 3 // 2
			else:
				answer = nums1[mid1]
		return answer

#2 assume len(nums1, nums2) isEven


#3 Combine #1 & #2
def findMedianSortedArrays(self, nums1, nums2):
	if nums1[mid1] > nums2[mid2]:

	elif nums1[mid1] < nums2[mid2]:

	else:
		if len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
			return nums1[mid1]
		else

#4 btute force
"""
Wrong Answer
Details
Playground Debug
Input
[1,2]
[3,4]
Output
1.50000
Expected
2.5
"""
	def findMedianSortedArrays(self, nums1, nums2):
    def Combine2SortedArrays(l1,l2):			
        # if len(l2)>len(l1): #l1 should be longer
        # if l2[0]<l1[0]: #l2[0] should be smaller
        #     l1, l2 = l2, l1
        l0 = []
        for i, j in enumerate(l2):
            for l, k in enumerate(l1):
                if k < j:
                    l0.append(k)
                else:
                    l0.append(j)
                    break 
            if len(l1) <= l +1:
                l1 = []
            else:
                l1 = l1[l+1:]
            if len(l2) <= i +1:
                l2 = []
            else:
                l2 = l2[i:]
            l0.append(j)
        return l0
    nums_combined = Combine2SortedArrays(nums1,nums2)
    if len(nums_combined)%2 == 1:
        return float(nums_combined[len(nums_combined)//2])
    else:
        return (nums_combined[len(nums_combined)//2]+nums_combined[(len(nums_combined)//2)-1])/2.0



# Test
## Functional Test
"""
Condition:

"""


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