# ToDo:

"""
961. N-Repeated Element in Size 2N Array
Easy

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Note:

    4 <= A.length <= 10000
    0 <= A[i] < 10000
    A.length is even
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
## test part
class Solution:
    def repeatedNTimes(self, A):
        """
        A: List[int]
        rtype: int
        """
        
## code here
#1
"""
Success
Runtime: 240 ms, faster than 32.76% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 14 MB, less than 97.96% of Python3 online submissions for N-Repeated Element in Size 2N Array.
"""
class Solution:
    def repeatedNTimes(self, A):
        from collections import Counter
        A = Counter(A)
        return A.most_common(1)[0][0]


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [[1,2,3,3], [2,1,2,5,3,2], [5,1,5,2,5,3,5,4]]
    expected_output = [3, 2, 5]
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