# ToDo:

"""
748. Shortest Completing Word
Easy

Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Note:
    licensePlate will be a string with length in range [1, 7].
    licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
    words will have a length in the range [10, 1000].
    Every words[i] will consist of lowercase letters, and have length in range [1, 15].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
## test part
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        licensePlate: str
        words: List[str]
        rtype: str
        """

## code here
#1
"""
Success
Runtime: 128 ms, faster than 12.97% of Python3 online submissions for Shortest Completing Word.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Shortest Completing Word.
"""
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        licensePlate = licensePlate.lower()
        alph = set([chr(x) for x in range(97,123)])
        truely = ''
        for c in licensePlate:
            if c in alph:
                truely += c

        res = []
        shortest = float('inf')
        from collections import Counter
        t = Counter(truely)
        for w in words: 
            if not (t-Counter(w.lower())) and shortest > len(w):
                res.append(w)
                shortest = len(w)
        for w in res:
            if len(w) == shortest: return w


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = ["1s3 PSt", "1s3 456"]
    input2 = [["step", "steps", "stripe", "stepple"], ["looks", "pest", "stew", "show"]]
    expected_output = ["steps", "pest"]
    for i in range(len(input1)):
        if shortestCompletingWord(input1[i], input2[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', shortestCompletingWord(input1[i], input2[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(shortestCompletingWord(input1[-1], input2[-1]))
    

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