# ToDo:

"""
705. Design HashSet
Easy

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

    add(value): Insert a value into the HashSet. 
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.


Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)


Note:

    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def add(self, key: int) -> None:
        

    def remove(self, key: int) -> None:
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
## test part

## code here
#1
"""
Success
Runtime: 1608 ms, faster than 8.75% of Python3 online submissions for Design HashSet.
Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Design HashSet.
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = []
        

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash_set: return True
        else: return False 

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