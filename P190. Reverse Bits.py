# ToDo:

"""
190. Reverse Bits
Easy

Reverse bits of a given 32 bits unsigned integer. 

Example 1:
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:
If this function is called many times, how would you optimize it?
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reverseBits(self, n: int) -> int:
        
## test part
def reverseBits(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
"""
n: 43261596
Your input :00000010100101000001111010011100
Output: 15065253 (00000000111001011110000010100101)
Expected: 964176192 (00111001011110000010100101000000)

Success
Runtime: 16 ms, faster than 99.65% of Python3 online submissions for Reverse Bits.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Bits.
"""
def reverseBits(n):
	return int(str(bin(n))[2:][::-1]+'0'*(34-len(bin(n))), base=2)
	
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