# ToDo:

"""
1160. Find Words That Can Be Formed by Characters
Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Note:
    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    All strings contain lowercase English letters only.

Hint:
    1.Solve the problem for each string in words independently.
    2.Now try to think in frequency of letters.
    3.Count how many times each character occurs in string chars.
    4.To form a string using characters from chars, the frequency of each character in chars must be greater than or equal the frequency of that character in the string to be formed.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
## test part
class Solution:
    def countCharacters(self, words, chars):
        """
        words: List[str]
        chars: str
        rtype: int
        """
        
## code here
#1
"""
Success
Runtime: 316 ms, faster than 18.18% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
"""
class Solution:
    def countCharacters(self, words, chars):
        from collections import Counter
        chars_c = Counter(chars)
        res = 0
        for w in words:
            if not Counter(w) - chars_c:
                res += len(w)
        return res


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [["cat","bt","hat","tree"], ["hello","world","leetcode"]]
    input2 = ["atach", "welldonehoneyr"]
    expected_output = [6, 10]
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