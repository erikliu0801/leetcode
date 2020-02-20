# ToDo:

"""
690. Employee Importance
Easy

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11. 

Note:

    One employee has at most one direct leader and may have several subordinates.
    The maximum number of employees won't exceed 2000.
"""
# Conditions & Concepts
"""
[id, importance, subordinate(s)]
"""
# Code
## submit part
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
## test part
class Solution:
    def getImportance(self, employees, id):
        """
        employees: List['Employee']
        id: int
        rtype: int
        """

## code here
#1
"""
Success
Runtime: 144 ms, faster than 99.69% of Python3 online submissions for Employee Importance.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Employee Importance.
"""
class Solution:
    def getImportance(self, employees, id):
        id_e = {}
        sum_val = 0
        sub_i = []
        for e in employees:
            id_e[e.id] = e

        if id in id_e:
            target = id_e[id]
            sum_val = target.importance
            sub_i = target.subordinates

        while sub_i:
            for i in sub_i.copy():
                sum_val += id_e[i].importance
                sub_i += id_e[i].subordinates
                sub_i.remove(i)
        return sum_val


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