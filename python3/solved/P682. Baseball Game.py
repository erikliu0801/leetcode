# ToDo:

"""
682. Baseball Game
Easy

You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

    Integer (one round's score): Directly represents the number of points you get in this round.
    "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
## test part
class Solution:
    def calPoints(self, ops):
        """
        ops: List[str]
        rtype: int
        """
        
## code here
#1
class Solution:
    def calPoints(self, ops):
        score = 0
        rounds = []
        for op in ops:
            if op == "D": 
                if rounds: score += rounds[-1] *2
            elif op == "+": 
                score += sum(rounds[-2:])
            elif op == "C": 
                if rounds: score -= rounds[-1]
                rounds = rounds[:-1]
            else:
                rounds.append(int(op))
                score += int(op)
        return score

#1.1
"""
Success
Runtime: 40 ms, faster than 54.60% of Python3 online submissions for Baseball Game.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Baseball Game.
"""
class Solution:
    def calPoints(self, ops):
        rounds = []
        for op in ops:
            if op == "D": 
                if rounds: rounds.append(rounds[-1]*2)
            elif op == "+": 
                rounds.append(sum(rounds[-2:]))
            elif op == "C": 
                if rounds: rounds.pop()
            else:
                rounds.append(int(op))
        return sum(rounds)


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [["5","2","C","D","+"], ["5","-2","4","C","D","9","+","+"]]
    expected_output = [30, 27]
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