# ToDo:

"""
888. Fair Candy Swap
Easy

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]

Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]

Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]

Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]

Note:

    1 <= A.length <= 10000
    1 <= B.length <= 10000
    1 <= A[i] <= 100000
    1 <= B[i] <= 100000
    It is guaranteed that Alice and Bob have different total amounts of candy.
    It is guaranteed there exists an answer.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
## test part
def fairCandySwap(A, B):
    """
    A: List[int]
    B: List[int]
    rtype: List[int]
    """

## code here
#1
"""
Success
Runtime: 5856 ms, faster than 13.99% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 15.7 MB, less than 81.08% of Python3 online submissions for Fair Candy Swap.
"""
def fairCandySwap(A, B):
    balance = (sum(A) + sum(B)) // 2
    gapA = balance - sum(A)
    for ele in A:
        if (ele + gapA) in B:
            return [ele, ele + gapA]




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