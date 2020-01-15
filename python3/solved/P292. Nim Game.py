# ToDo:

"""
292. Nim Game
Easy
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def canWinNim(self, n: int) -> bool:
        
## test part
def canWinNim(n):
	"""
	n: int
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 24 ms, faster than 86.06% of Python3 online submissions for Nim Game.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Nim Game.
"""
def canWinNim(n):
	return n % 4 != 0

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
			print("Wrong!!!")
			print(func(input1[i]))
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