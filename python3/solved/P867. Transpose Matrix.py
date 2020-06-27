# ToDo:

"""
867. Transpose Matrix
Easy

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],
        [4,5,6],
        [7,8,9]]
Output: [[1,4,7],
        [2,5,8],
        [3,6,9]]

Example 2:

Input: [[1,2,3],
        [4,5,6]]
Output: [[1,4],
        [2,5],
        [3,6]]

Note:

    1 <= A.length <= 1000
    1 <= A[0].length <= 1000
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
## test part
def transpose(A):
    """
    A: List[List[int]]
    rtype: List[List[int]]:
    """

## code here
#1
"""
Success
Runtime: 64 ms, faster than 98.53% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.6 MB, less than 14.01% of Python3 online submissions for Transpose Matrix.
"""
def transpose(A):
    rowNum = len(A)
    if rowNum != 0: colNum = len(A[0])
    else: return []
    # trans = [ [0] * rowNum  ] * colNum
    # trans = [ [] ] * colNum # shallow copy issue
    trans = []
    for i in range(colNum):
        trans.append([])
    for ri in range(rowNum):
        for ci in range(colNum):
            trans[ci].append(A[ri][ci])
    return trans



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