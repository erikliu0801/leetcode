# ToDo:

"""
806. Number of Lines To Write String
Easy

We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.

 

Example :
Input: 
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation: 
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.

Example :
Input: 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
Output: [2, 4]
Explanation: 
All letters except 'a' have the same length of 10, and 
"bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
For the last 'a', it is written on the second line because
there is only 2 units left in the first line.
So the answer is 2 lines, plus 4 units in the second line.

Note:

    The length of S will be in the range [1, 1000].
    S will only contain lowercase letters.
    widths is an array of length 26.
    widths[i] will be in the range of [2, 10].

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        
## test part
def numberOfLines(widths, S):

## code here
#1
"""
Success
Runtime: 52 ms, faster than 6.25% of Python3 online submissions for Number of Lines To Write String.
Memory Usage: 14 MB, less than 7.56% of Python3 online submissions for Number of Lines To Write String.
"""
def numberOfLines(widths, S):
    units = 0
    lines = 1
    for c in S:
        units += widths[ord(c) - 97]
        if units > 100:
            lines += 1
            units = widths[ord(c) - 97]
    return [lines, units]


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