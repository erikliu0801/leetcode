# ToDo:

"""
1025. Divisor Game
Easy

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < N and N % x == 0.
    Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
 
Note:
    1 <= N <= 1000
"""
# Conditions & Concepts
"""
1 <= N <= 1000
0 < x < N and N % x == 0
N - x
"""
# Code
## submit part
class Solution:
    def divisorGame(self, N: int) -> bool:
        
## test part
def divisorGame(N):
	"""
	N: int
	rtype: bool
	"""
## code here
#1
def divisorGame(N):
	def helper(M):
		devisors = set()
		import math
		for i in range(1, int(math.sqrt(M))+1):
			if (i<M) and (M//i != 0) and (M % i == 0):
				devisors.add(i)
				if M//i < M:
					devisors.add(M//i)
		if devisors == set():
			return -1
		return M - max(devisors)

	if helper(N) == -1: return False
	if helper(helper(N)) == -1 : return True
	return False

#1.1
def divisorGame(N):
	def helper(M):
		if M == 1: return 1
		devisors = set()
		import math
		for i in range(1, int(math.sqrt(M))+1):
			if (i<M) and (M//i != 0) and (M % i == 0):
				devisors.add(i)
				if M//i < M:
					devisors.add(M//i)
		return M - max(devisors)
	chalkboard = [N]	
	while N > 1:
		N = helper(N)
		chalkboard.append(N)
	if chalkboard.index(1) %2 == 1:
		return False
	return True

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = [1, 2, 3, 4, 5]
	expected_output = [False, True, False, True, False]
	for i in range(len(input1)):
		if divisorGame(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', divisorGame(input1[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(divisorGame(input1[-1]))
	

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