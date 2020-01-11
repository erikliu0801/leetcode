# ToDo:

"""
455. Assign Cookies
Easy
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive. gi > 0
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

"""
# Conditions & Concepts
"""
g.sort()
s.sort()

satisfied = 0
for j in s:
	for i in g:
		if j >= i:
			satisfied += 1
			g.remove(i)
return satisfied



"""
# Code
## submit part
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
## test part
def findContentChildren(g, s):
	"""
	g: List[int]
	s: List[int]
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 772 ms, faster than 7.02% of Python3 online submissions for Assign Cookies.
Memory Usage: 14.4 MB, less than 71.43% of Python3 online submissions for Assign Cookies.

"""
def findContentChildren(g, s):
	g.sort()
	s.sort()

	satisfied = 0
	for j in s:
		for i in g:
			if j >= i:
				satisfied += 1
				g.remove(i)
				break
	return satisfied

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