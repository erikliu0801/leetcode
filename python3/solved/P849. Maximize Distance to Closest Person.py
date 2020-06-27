# ToDo:

"""
849. Maximize Distance to Closest Person
Easy

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Constraints:
2 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
## test part
def maxDistToClosest(seats):
    """
    seats: List[int]
    rtype: int:
    """
        
## code here
#1
"""
Success
Runtime: 140 ms, faster than 70.76% of Python3 online submissions for Maximize Distance to Closest Person.
Memory Usage: 14.2 MB, less than 89.90% of Python3 online submissions for Maximize Distance to Closest Person.
"""
def maxDistToClosest(seats):
    def maxDistance(dist):
        if dist % 2 != 0:
            distNums.append(dist//2 + 1)
        else:
            distNums.append(dist//2)

    firstIndex = seats.index(1)
    lastIndex = len(seats) - 1 - seats[::-1].index(1)
    middle = seats[firstIndex + 1: lastIndex]
    distNums = [firstIndex, seats[::-1].index(1)]
    dist = 0 
    for seat in middle:
        if seat == 1:
            maxDistance(dist)
            dist = 0
        else:
            dist += 1
    if dist != 0: maxDistance(dist)
    return max(distNums)


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