# ToDo:

"""
1021. Remove Outermost Parentheses
Easy

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()()) (())"
Output: "()() ()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: "(()()) (()) (() (()))"
Output: "()() () () (())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:
    S.length <= 10000
    S[i] is "(" or ")"
    S is a valid parentheses string

Hint:
    Can you find the primitive decomposition? The number of ( and ) characters must be equal.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
## test part
class Solution:
    def removeOuterParentheses(self, S):
        """
        S: str
        rtype: str
        """
        
## code here
#1
"""
Success
Runtime: 32 ms, faster than 90.88% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
"""
class Solution:
    def removeOuterParentheses(self, S):
        res = ""
        left, right = 0, 0
        for c in S:
            if c == "(":
                if left > 0: res += c
                left += 1
            elif c == ")":
                right += 1
                if left == right: left, right = 0, 0
                else: res += c
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