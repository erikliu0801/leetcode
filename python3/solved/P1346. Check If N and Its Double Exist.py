# ToDo:

"""
1346. Check If N and Its Double Exist
Easy

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
## test part
def checkIfExist(arr):
	"""
	arr: List[int]
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input: [-2,0,10,-19,4,6,-8]
Output: true
Expected: false

Wrong Answer
Input: [0,0]
Output: false
Expected: true

Success
Runtime: 64 ms, faster than 19.84% of Python3 online submissions for Check If N and Its Double Exist.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Check If N and Its Double Exist.
"""
def checkIfExist(arr):
	arr.sort()	
	for c in arr:
		if c == 0 and arr.count(0) > 1: return True
		if (c != 0) and (c*2 in arr) : return True
		if c*2 > arr[-1]: break
	return False

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