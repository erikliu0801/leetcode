# ToDo:

"""
720. Longest Word in Dictionary
Easy

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
## test part
class Solution:
    def longestWord(self, words):
        """
        words: List[str]
        rtype: str
        """

## code here
#1
"""
Wrong Answer
Input:["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
Output:"lunch"
Expected:"breakfast"

Wrong Answer
Input: ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
Output: ""
Expected: "e"

Success
Runtime: 2872 ms, faster than 5.05% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.
"""
class Solution:
    def longestWord(self, words):
        words.sort(reverse = True)
        res = []
        alph = []
        longest = 0
        for w in words:
            if len(w) == 1:
                alph.append(w)
            if longest > len(w):
                continue
            for j in range(1,len(w)):
                if w[:j] not in words:
                    break
                if j == len(w) -1:
                    res.append(w)
                    longest = len(w)
        if res: return res[-1]
        elif alph: return alph[-1]
        else: return ''


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [["w","wo","wor","worl", "world"], 
    ["a", "banana", "app", "appl", "ap", "apply", "apple"], 
    ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"], 
    ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]]
    expected_output = ["world", "apple", "breakfast", "e"]
    for i in range(len(input1)):
        if longestWord(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', longestWord(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(longestWord(input1[-1]))
    

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