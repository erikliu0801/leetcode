# ToDo:

"""
605. Can Place Flowers
Easy

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Note:
    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
## test part
def canPlaceFlowers(flowerbed, n):
	"""
	flowerbed: List[int]
	n: int
	rtype: bool
	"""
## code here
#1
"""
Wrong Answer
Input
[1,0,1,0,1,0,1], 1
Output: true
Expected: false

Runtime Error: ValueError: 1 is not in list
Last executed input: [1,0,0,0,1,0,0], 2

Success
Runtime: 788 ms, faster than 5.05% of Python3 online submissions for Can Place Flowers.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.
"""
def canPlaceFlowers(flowerbed, n):
	rest_place = []
	max_added_flowers = 0
	existed_flowers = flowerbed.count(1)
	while flowerbed:
		if flowerbed[0] == 1:
			flowerbed = flowerbed[2:]
			existed_flowers -= 1
			continue
		if existed_flowers > 0:
			rest_place.append(flowerbed[:flowerbed.index(1)-1])
			flowerbed = flowerbed[flowerbed.index(1)+2:]
			existed_flowers -= 1
		else:
			rest_place.append(flowerbed)
			break
	for place in rest_place:
		max_added_flowers += (len(place)+1) // 2
	return n <= max_added_flowers

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_flowerbed = [[1,0,0,0,1], [1,0,0,0,1], [1,0,1,0,1,0,1], [1,0,1,0,1,0,0,1], [1,0,1,0,1,0,0,0,1], [1,0,0,0,1,0,0]]
	input_n = [1, 2, 1, 1, 1, 2]
	expected_output = [True, False, False, False, True, True]
	for i in range(len(input_flowerbed)):
		if canPlaceFlowers(input_flowerbed[i], input_n[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', canPlaceFlowers(input_flowerbed[i], input_n[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(canPlaceFlowers(input_flowerbed[-1], input_n[-1]))
	

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