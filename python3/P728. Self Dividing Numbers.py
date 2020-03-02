# ToDo:

"""
728. Self Dividing Numbers
Easy

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:

Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.


Hint:
For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), then checking that each digit is nonzero and divides the original number.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        pass
        
## test part
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        left: int
        right: int
        rtype: List[int]
        """
        
## code here
#1
"""
Success
Runtime: 44 ms, faster than 79.28% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Self Dividing Numbers.
"""
class Solution:
def selfDividingNumbers(left, right):
    res = []
    for i in range(left, right +1):
        sdnum = True
        for j in str(i):
            if j == '0' or i % int(j) != 0:
                sdnum = False
                break
        if sdnum: res.append(i)
    return res




# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = [1]
    input2 = [22]
	expected_output = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]]
	for i in range(len(input1)):
		if selfDividingNumbers(input1[i], input2[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', selfDividingNumbers(input1[i], input2[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(selfDividingNumbers(input1[-1], input2[-1]))
	

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