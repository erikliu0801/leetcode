# ToDo:

"""
937. Reorder Data in Log Files
Easy

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs. 

Constraints:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
## test part
def reorderLogFiles(logs):
	"""
	logs: List[str]
	rtype: List[str]
	"""
## code here
#1
def reorderLogFiles(logs):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_logs = [ ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]]
	expected_output = [["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]]
	for i in range(len(input_logs)):
		if reorderLogFiles(input_logs[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', reorderLogFiles(input_logs[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(reorderLogFiles(input_logs[-1]))
	

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