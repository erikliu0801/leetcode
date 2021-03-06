# ToDo:

"""
443. String Compression
Easy

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
 

Follow up:
Could you solve it using only O(1) extra space?
 

Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

 

Note:

    All characters have an ASCII value in [35, 126].
    1 <= len(chars) <= 1000.



"""
# Conditions & Concepts
"""

if count > 1 then insert the count per digit after alph
remove alph count-1 times
"""
# Code
## submit part
class Solution:
    def compress(self, chars: List[str]) -> int:
        
## test part
def compress(chars):
	"""
	chars: List[str]
	rtype: int
	"""
## code here
#1
def compress(chars):
	alph = str()
	position_nums = list()
	for i, j in enumerate(chars):
		if j != alph or i == len(chars)-1:
			if i != 0:
				position_nums.append((start, i))
			if j == alph:
				chars.pop(i)
				break
			alph = j
			start = i
		else:
			chars.pop(i)

	return len(chars)

#1.1
def compress(chars):
	alph = str()
	start = 0
	for i, j in enumerate(chars.copy()):
		if j != alph or i == len(chars.copy())-1:
			if i != 0 and i - start not in [0,1]:
				for m, count in enumerate(list(str(i-start))):
					chars.insert(start+1+m, count)
			if j == alph:
				chars.remove(j)
				break
			alph = j
			start = i
		else:
			chars.remove(j)
	return len(chars)

#1.2
def compress(chars):
	alph = chars[0]
	start = 0
	alph_count_nums = list()
	for i, j in enumerate(chars):
		if i == len(chars)-1:
			if j != alph:
				alph_count_nums.append((alph, i-start))
				alph_count_nums.append((j, 1))
			else:
				alph_count_nums.append((alph, i-start+1))
		elif j != alph:
			alph_count_nums.append((alph, i-start))
			alph = j
			start = i
	#
	chars = list()
	for alph, count in alph_count_nums:
		chars.append(alph)
		for c in list(str(count)):
			chars.append(c)
	#
	return len(chars)

#1.3
"""
Runtime Error
["a"]

Success
Runtime: 60 ms, faster than 47.09% of Python3 online submissions for String Compression.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for String Compression.
"""
def compress(chars):
	alph = chars[0]
	start = 0
	alph_count_nums = list()
	for i, j in enumerate(chars):
		if i == len(chars)-1:
			if j != alph:
				alph_count_nums.append((alph, i-start))
				alph_count_nums.append((j, 1))
			else:
				alph_count_nums.append((alph, i-start+1))
		elif j != alph:
			alph_count_nums.append((alph, i-start))
			alph = j
			start = i
	#
	i = 0
	for alph, count in alph_count_nums:
		chars[i] = alph
		i += 1
		if count != 1:
			for c in list(str(count)):
				chars[i] = c
				i += 1
	for _ in range(len(chars)-i):
		chars.pop()
	#
	return len(chars)

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