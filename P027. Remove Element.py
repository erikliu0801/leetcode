# ToDo:

"""
27. Remove Element
Easy

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


"""
# Concepts


# Code
## submit part
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
## test part
def removeElement(nums,val):
	"""
	nums = List
	val = int
	rtype = int
	"""
## code here
#1
"""
Success
Runtime: 32 ms, faster than 84.68% of Python3 online submissions for Remove Element.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Element.
"""
def removeElement(nums,val):
	count = 0
	for i, j in enumerate(nums):
		if j != val:
			nums[count] = nums[i]
			count += 1
	nums = nums[:count]
	return len(nums)



# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input_nums = [[3,2,2,3]]
	input_val = [3]
	expected_output = [2]
	expected_nums = [[2,2]]
	for i, j in enumerate(input_nums):
		if removeElement(input_nums[i],input_val[i]) != expected_output[i]:
			print("Wrong!!!")
			print(removeElement(input_nums[i],input_val[i]))
		else:
			print("Right")
	# print(removeElement(input_nums[-1],input_val[-1]))
	

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