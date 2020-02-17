# ToDo:

"""
922. Sort Array By Parity II
Easy

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,2,5,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted. 

Note:

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
## test part
def sortArrayByParityII(A):
	"""
	A: List[int]
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 236 ms, faster than 40.31% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 15.1 MB, less than 95.65% of Python3 online submissions for Sort Array By Parity II.
"""
def sortArrayByParityII(A):
	odd = []
	even = []
	for i ,c in enumerate(A):
		if (i % 2 == 0) and (c % 2 != 0) :
			A[i] = True #even
			odd.append(c)
		elif (i % 2 == 1) and (c % 2 != 1) :
			A[i] = False #odd
			even.append(c) 
	for i ,c in enumerate(A):
		if c is False:
			A[i] = odd.pop()
		elif c is True:
			A[i] = even.pop()
	return A


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = [[4,2,5,7]]
	expected_output = []
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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