# ToDo:

"""
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
# Concepts
"""
1. create needed Rows
2. Reallocate
3. Combine
"""

# Code
## submit part
class Solution:
    def convert(self, s: str, numRows: int) -> str:
## test part

## code here
#1
"""
one way instead of zig zag
"""
def convert(s, numRows):
	#
	needed_List = []
	for i in range(numRows):
		needed_List.append([])
	#
	for i, j in enumerate(list(s)):
		needed_List[i%numRows].append(j)
	#
	answer =''
	for i, j in enumerate(needed_List):
		for i in needed_List[i]:
			answer += i
	return answer

#1.2
"""
go-and-back way still not zig zag
"""
def convert(s, numRows):
	#
	needed_List = []
	for i in range(numRows):
		needed_List.append([])
	#
	for i, j in enumerate(list(s)):
		if (i//numRows)%2 == 0:
			needed_List[i%numRows].append(j)
		else:
			needed_List[-1-(i%numRows)].append(j)
	#
	answer =''
	for i, j in enumerate(needed_List):
		for i in needed_List[i]:
			answer += i
	return answer

#1.3
"""
Wrong Answer
Input:"PAYPALISHIRING",4
Output:"PINASGYAHRPLII"
Expected:"PINALSIGYAHRPI" => ok

Success
Details
Runtime: 60 ms, faster than 80.54% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
"""
def convert(s, numRows):
	#
	if numRows == 1:
		answer = s
	else:
		needed_List = []
		for i in range(numRows):
			needed_List.append([])
		#
		onetime_steps = numRows *2 -2
		for i, j in enumerate(list(s)):
			numofStep = i%onetime_steps
			if numofStep < numRows :
				needed_List[numofStep].append(j)
			else:
				l = numofStep - numRows
				needed_List[-2-l].append(j) #numRows>2
		#
		answer =''
		for i, j in enumerate(needed_List):
			for i in needed_List[i]:
				answer += i
	return answer

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	string = ["PAYPALISHIRING","PAYPALISHIRING"]
	numRows = [3, 4]
	expected_output = ["PAHNAPLSIIGYIR","PINALSIGYAHRPI"]
	print(convert(string[0],numRows[0]))

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