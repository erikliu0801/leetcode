# ToDo:

"""
191. Number of 1 Bits
Easy

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

 

Note:

    Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

 

Follow up:

If this function is called many times, how would you optimize it?


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def hammingWeight(self, n: int) -> int:
        
## test part
def hammingWeight(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 48 ms, faster than 7.04% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.
"""
def hammingWeight(n):
	return str(bin(n)).count('1')

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