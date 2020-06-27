# ToDo:

"""
905. Sort Array By Parity
Easy

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

    1 <= A.length <= 5000
    0 <= A[i] <= 5000


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
## test part
def sortArrayByParity(A):
    """
    A: List[int]
    rtype: List[int]
    """

## code here
#1
"""
Success
Runtime: 96 ms, faster than 22.90% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.4 MB, less than 35.36% of Python3 online submissions for Sort Array By Parity.
"""
def sortArrayByParity(A):
    res = []
    for n in A:
        if n % 2 == 0:
            res.insert(0, n)
        else:
            res.append(n)
    return res


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