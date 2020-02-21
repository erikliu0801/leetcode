# ToDo:

"""
884. Uncommon Words from Two Sentences
Easy

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Note:

    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
## test part
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        A: str
        B: str
        rtype: List[str]
        """
        
## code here
#1
"""
Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""
# class Solution:
#     def uncommonFromSentences(self, A, B):
#         A = set(A.split(' '))
#         B = set(B.split(' '))
#         return [x for x in (A-B) | (B-A)]

#1.1
"""
Wrong Answer
Input
"s z z z s"
"s z ejt"
Output
["s","ejt"]
Expected
["ejt"]

Success
Runtime: 36 ms, faster than 13.30% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
"""
class Solution:
    def uncommonFromSentences(self, A, B):
        from collections import Counter
        A = Counter(A.split(' '))
        B = Counter(B.split(' '))
        return [k for k, v in ((A-B) | (B-A)).items() if v == 1 and k not in (B&A)]



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = ["this apple is sweet", "apple apple"]
    input2 = ["this apple is sour", "banana"]
    expected_output = [["sweet","sour"], ["banana"]]
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