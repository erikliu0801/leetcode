# ToDo:

"""
860. Lemonade Change
Easy

At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

 

Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: [5,5,10]
Output: true

Example 3:

Input: [10,10]
Output: false

Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.

Note:

    0 <= bills.length <= 10000
    bills[i] will be either 5, 10, or 20.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
## test part
def lemonadeChange(bills):
    """
    bills: List[int]
    rtype: bool:
    """

## code here
#1
"""
Success
Runtime: 156 ms, faster than 42.07% of Python3 online submissions for Lemonade Change.
Memory Usage: 14 MB, less than 39.59% of Python3 online submissions for Lemonade Change.
"""
def lemonadeChange(bills):
    pocket = {
        5:0,
        10:0
    }
    for bill in bills:
        if bill == 5:
            pocket[5] += 1

        elif bill == 10:
            if pocket[5] == 0: return False
            pocket[5] -= 1
            pocket[10] += 1

        elif bill == 20:
            if pocket[10] >= 1 and pocket[5] >= 1:
                pocket[5] -= 1
                pocket[10] -= 1
            elif pocket[5] >= 3:
                pocket[5] -= 3
            else:
                return False
    return True


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