# ToDo:

"""
599. Minimum Index Sum of Two Lists
Easy

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Note:

    The length of both lists will be in the range of [1, 1000].
    The length of strings in both lists will be in the range of [1, 30].
    The index is starting from 0 to the list length minus 1.
    No duplicates in both lists.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
## test part
class Solution:
    def findRestaurant(self, list1, list2):
        """
        list1: List[str]
        list2: List[str]
        rtype: List[str]:
        """

## code here
#1
"""
Wrong Answer
Input:
["Shogun","Tapioca Express","Burger King","KFC"]
["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["Shogun"]
Expected: ["KFC","Burger King","Tapioca Express","Shogun"]

Success
Runtime: 196 ms, faster than 32.36% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Minimum Index Sum of Two Lists.
"""
class Solution:
    def findRestaurant(self, list1, list2):
        
        res = []
        common = set(list1) & set(list2)
        common_priority = {}
        for r in common:
            common_priority[r] = list1.index(r)+list2.index(r)
        first = min(common_priority.values())
        for r, p in common_priority.items():
            if p == first: res.append(r)
        return res 


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input_list1 = [["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Shogun","Tapioca Express","Burger King","KFC"]]
    input_list2 = [["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"], ["KFC", "Shogun", "Burger King"], ["KFC","Burger King","Tapioca Express","Shogun"]]
    expected_output = [["Shogun"], ["Shogun"], ["KFC","Burger King","Tapioca Express","Shogun"]]
    for i in range(len(input_list1)):
        if findRestaurant(input_list1[i], input_list2[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', findRestaurant(input_list1[i], input_list2[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(findRestaurant(input_list1[-1], input_list2[-1]))
    

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