# ToDo:

"""
908. Smallest Range I
Easy

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:

    1 <= A.length <= 10000
    0 <= A[i] <= 10000
    0 <= K <= 10000

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        
## test part
def smallestRangeI(A, K):
    """
    A: List[int], K: int) -> int:
    """

## code here
#1 return B
"""
Wrong Answer
Input: [3,1,10], 4
Output: 2
Expected: 1
"""
def smallestRangeI(A, K):
    balance = sum(A) // len(A)
    for i, n in enumerate(A):
        if n > balance:
            if  (n - balance) < K:
                A[i] = balance 
            else:
                A[i] -= K

        elif n < balance:
            if  (balance - n) < K:
                A[i] = balance 
            else:
                A[i] += K

    return abs(max(A) - min(A))

#1.1
"""
Wrong Answer
Input: [9,9,2,8,7], 4
Output: 1
Expected: 0
"""
def smallestRangeI(A, K):
    from decimal import Decimal, ROUND_HALF_UP
    balance = Decimal(str(sum(A) / len(A))).quantize(Decimal('1'), ROUND_HALF_UP)
    for i, n in enumerate(A):
        if n > balance:
            if  (n - balance) < K:
                A[i] = balance 
            else:
                A[i] -= K

        elif n < balance:
            if  (balance - n) < K:
                A[i] = balance 
            else:
                A[i] += K

    return abs(max(A) - min(A))

#2
"""
Success
Runtime: 188 ms, faster than 9.03% of Python3 online submissions for Smallest Range I.
Memory Usage: 15 MB, less than 26.07% of Python3 online submissions for Smallest Range I.
"""
def smallestRangeI(A, K):
    maxNum = max(A)
    minNum = min(A)
    if ( maxNum - minNum ) < K *2: return 0
    else: return maxNum - minNum - K*2 

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input_A = [[1], [0,10], [1,3,6], [9,9,2,8,7]]
    input_K = [0, 2, 3, 4]
    expected_output = [0, 6, 0, 1]
    for i in range(len(input_A)):
        if smallestRangeI(input_A[i], input_K[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', smallestRangeI(input_A[i], input_K[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(smallestRangeI(input_A[i], input_K[i]))
    

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