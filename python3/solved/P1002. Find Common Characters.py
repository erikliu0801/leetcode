# ToDo:

"""
1002. Find Common Characters
Easy

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Note:

    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
## test part
class Solution:
    def commonChars(self, A):
        """
        A: List[str]
        rtype: List[str]
        """
        
## code here
#1
class Solution:
    def commonChars(self, A):
        from collections import Counter
        
        w_count = Counter()
        for w in A:
            w_count += Counter(w)

        res = []
        for k, v in w_count.items():
            if v >= 3: res.append(k)

        return res

#1.1
"""
Success
Runtime: 48 ms, faster than 65.30% of Python3 online submissions for Find Common Characters.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Find Common Characters.
"""
class Solution:
    def commonChars(self, A):
        if not A: return []
        from collections import Counter
        common = Counter(A[0])

        for w in A[1:]:
            common = common&Counter(w)
        res = []
        for k, v in common.items():
            res += [k] *v

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