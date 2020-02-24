# ToDo:

"""
1207. Unique Number of Occurrences
Easy

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true 

Constraints:

    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
## test part
class Solution:
    def uniqueOccurrences(self, arr):
        """
        arr: List[int]
        rtype: bool
        """
        
## code here
#1
"""
Success
Runtime: 28 ms, faster than 94.14% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
"""
class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter
        occurrences = set()
        a = Counter(arr)
        for v in a.values():
            if v in occurrences: return False
            occurrences.add(v)
        return True


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [[1,2,2,1,1,3], [1,2], [-3,0,1,-3,1,1,1,-3,10,0]]
    expected_output = [True, False, True]
    for i in range(len(input1)):
        if uniqueOccurrences(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', uniqueOccurrences(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(uniqueOccurrences(input1[-1]))
    

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