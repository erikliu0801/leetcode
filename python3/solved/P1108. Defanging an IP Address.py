# ToDo:

"""
1108. Defanging an IP Address
Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

 

Constraints:

    The given address is a valid IPv4 address.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
## test part
def defangIPaddr(address):
	"""
	address: str
	rtype: str
	"""
## code here
#1
"""
Success
Runtime: 24 ms, faster than 83.98% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
"""
def defangIPaddr(address):
	return address.replace(".","[.]")

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