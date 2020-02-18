# ToDo:

"""
1122. Relative Sort Array
Easy

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Constraints:

    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    Each arr2[i] is distinct.
    Each arr2[i] is in arr1.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
## test part
def relativeSortArray(arr1, arr2):
	"""
	arr1: List[int]
	arr2: List[int]
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 44 ms, faster than 28.97% of Python3 online submissions for Relative Sort Array.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.
"""
def relativeSortArray(arr1, arr2):
	arr_front = []
	s1 = set(arr1)
	for c in arr2:
		# if c in arr1: 
			arr_front.extend([c] * arr1.count(c))
			s1.remove(c)
	arr_end = []
	for c in s1:
		arr_end.extend([c] * arr1.count(c))
	arr_end.sort()
	return arr_front+arr_end


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_arr1 = [[2,3,1,3,2,4,6,7,9,2,19]]
	input_arr2 = [[2,1,4,3,9,6]]
	expected_output = [[2,2,2,1,4,3,3,9,6,7,19]]
	for i in range(len(input_arr1)):
		if relativeSortArray(input_arr1[i], input_arr2[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', relativeSortArray(input_arr1[i], input_arr2[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(relativeSortArray(input_arr1[-1], input_arr2[-1]))
	

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