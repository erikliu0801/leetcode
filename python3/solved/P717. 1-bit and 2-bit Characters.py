# ToDo:

"""
717. 1-bit and 2-bit Characters
Easy

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Note:
1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
## test part
def isOneBitCharacter(bits):
	"""
	bits: List[int]
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 44 ms, faster than 95.39% of Python3 online submissions for 1-bit and 2-bit Characters.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for 1-bit and 2-bit Characters.
"""
def isOneBitCharacter(bits):
	cd = 0
	for bit in bits[:-1]:
		if cd > 0:
			cd -= 1
			continue
		if bit == 1:
			cd = 1
	return cd == 0 

#1.1
"""
Success
Runtime: 44 ms, faster than 95.39% of Python3 online submissions for 1-bit and 2-bit Characters.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for 1-bit and 2-bit Characters.
"""
def isOneBitCharacter(bits):
	cd = False
	for bit in bits[:-1]:
		if cd:
			cd = False
			continue
		if bit == 1:
			cd = True
	return not cd

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_bits = [[1, 0, 0], [1, 1, 1, 0], [0], [1, 0], [0, 0]]
	expected_output = [True, False, True, False, True]
	for i in range(len(input_bits)):
		if isOneBitCharacter(input_bits[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', isOneBitCharacter(input_bits[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(isOneBitCharacter(input_bits[-1]))
	

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