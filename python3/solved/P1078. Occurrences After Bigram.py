# ToDo:

"""
1078. Occurrences After Bigram
Easy

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Note:

    1 <= text.length <= 1000
    text consists of space separated words, where each word consists of lowercase English letters.
    1 <= first.length, second.length <= 10
    first and second consist of lowercase English letters.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
## test part
class Solution:
    def findOcurrences(self, text, first, second):
        """
        text: str
        first: str
        second: str
        rtype: List[str]

        """
        
## code here
#1
"""
Success
Runtime: 28 ms, faster than 58.05% of Python3 online submissions for Occurrences After Bigram.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Occurrences After Bigram.
"""
class Solution:
    def findOcurrences(self, text, first, second):
        res = []

        t_re = text.split(' ')[::-1]
        if len(t_re) < 3: return res
        for i, w in enumerate(t_re[:-2]):
            if t_re[i+1] == second and t_re[i+2] == first:
                res = [w] + res

        return res


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = ["we will we will rock you"]
    input2 = ["we"]
    input3 = ["will"]
    expected_output = [["we","rock"]]
    for i in range(len(input1)):
        if findOcurrences(input1[i], input2[i], input3[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findOcurrences(input1[i], input2[i], input3[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(findOcurrences(input1[-1], input2[-1], input3[-1]))
    

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