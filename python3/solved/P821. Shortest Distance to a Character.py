# ToDo:

"""
821. Shortest Distance to a Character
Easy

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

"""
# Conditions & Concepts
"""
len(c) == 1



"""
# Code
## submit part
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
## test part
def shortestToChar(S, C):

## code here
#1
"""
after but not before

Wrong Answer
Runtime: 32 ms
Your input : "loveleetcode", "e"
Output : [3,2,1,0,1,0,0,4,3,2,1,0]
Expected : [3,2,1,0,1,0,0,1,2,2,1,0]
"""
def shortestToChar(S, C):
    distance = []
    step = 0 
    for i, c in enumerate(S):
        if c == C:
            distance.extend([i for i in range(step,-1,-1)])
            step = 0
        else:
            step += 1
    return distance

#1.1
"""
C not in the end of S
"""
def shortestToChar(S, C):
    def findNext(S, C):
        distance = []
        step = 0 
        for c in S:
            if c == C:
                distance.extend([i for i in range(step,-1,-1)])
                step = 0
            else:
                step += 1
        return distance

    dis1, dis2 = findNext(S,C), findNext(S[::-1], C)
    for i in range(len(dis1)-1):
        if dis1[i] > dis2[i]: 
            dis1[i] = dis2[i]
    return dis1

#2
"""
Success
Runtime: 48 ms, faster than 45.19% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14 MB, less than 38.62% of Python3 online submissions for Shortest Distance to a Character.
"""
def shortestToChar(S, C):
    def  mountainNums(num):
        nums = [i for i in(range(1, num//2 + 1))]
        numsRight = nums[::-1]
        if num % 2 == 1:
            nums += [ num//2 + 1 ]
        nums += numsRight
        return nums


    # first part: increase
    Cindex = S.index(C)
    dist = [i for i in range(Cindex, -1, -1)]
    if not S[Cindex+1:]: return dist

    # middle part : first increase then decrease
    step = 0
    for i in range(Cindex+1, len(S)):
        if S[i] == C:
            if step == 0: 
                dist += [0]
                continue
            dist += mountainNums(step) + [0]

            step = 0
        else:
            step += 1

    # last part : decrease
    dist += [i for i in range(1, step+1)]
    return dist



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