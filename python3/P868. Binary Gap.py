# ToDo:

"""
868. Binary Gap
Easy

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

Note:    1 <= N <= 10^9
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def binaryGap(self, N: int) -> int:
        
## test part
class Solution:
    def binaryGap(self, N):
        """
        N: int
        rtype: int
        """
        
## code here
#1
"""
Wrong Answer
Input: 13 '0b1101'
Output: 3
Expected: 2

Wrong Answer
Input: 21 '0b10101'
Output: 4
Expected: 2
"""
class Solution:
    def binaryGap(self, N):
        bi = bin(N)
        b1, b2 = bi.find('1'),  bi.rfind('1')
        if b1 == -1 or b1 == b2: return 0
        while bi[b1+1] == '1' and b2 > b1 +1:
            b1 += 1
        while bi[b2-1] == '1' and b1 < b2 - 1:
            b2 -= 1
        return b2 - b1


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [22, 5, 6, 8]
    expected_output = [2, 2, 1, 0]
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