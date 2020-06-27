# ToDo:

"""
896. Monotonic Array
Easy

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.


Example 1:

Input: [1,2,2,3]
Output: true

Example 2:

Input: [6,5,4,4]
Output: true

Example 3:

Input: [1,3,2]
Output: false

Example 4:

Input: [1,2,4,5]
Output: true

Example 5:

Input: [1,1,1]
Output: true

Note:

    1 <= A.length <= 50000
    -100000 <= A[i] <= 100000
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
## test part
    def isMonotonic(A):
        """
        A: List[int]
        rtype: bool
        """

## code here
#1
"""
Success
Runtime: 488 ms, faster than 94.36% of Python3 online submissions for Monotonic Array.
Memory Usage: 19.9 MB, less than 33.68% of Python3 online submissions for Monotonic Array.
"""
def isMonotonic(A):
    monoType = "undefined"
    if len(A) <= 1: return True
    pre = A[0]
    for n in A[1:]:
        if n != pre:
            if monoType == "undefined":
                if n > pre: monoType = "increasing"
                else: monoType = "decreasing"

            elif monoType == "increasing":
                if n < pre: return False

            elif monoType == "decreasing":
                if n > pre: return False

            pre = n

    return True






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