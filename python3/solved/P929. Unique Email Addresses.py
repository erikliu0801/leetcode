# ToDo:

"""
929. Unique Email Addresses
Easy

1. Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain '.'s or '+'s.

2. If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

3. If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

4. It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

Note:

    1 <= emails[i].length <= 100
    1 <= emails.length <= 100
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.
"""
# Conditions & Concepts
"""
local_name = lowercase letters,'.' ,'+'
"""
# Code
## submit part
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
## test part
def numUniqueEmails(emails):
	"""
	emails: List[str]
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 84 ms, faster than 12.79% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
"""
def numUniqueEmails(emails):
	local_name = ''
	uniqe_emails = set()
	for email in emails:
		for i, c in enumerate(email):
			if c == '.':
				continue
			elif c == '+':
				uniqe_emails.add(local_name + email[email.index('@'):])
				local_name = ''
				break
			elif c == '@':
				uniqe_emails.add(local_name + email[i:])
				local_name = ''
				break
			else:
				local_name += c
	return len(uniqe_emails)


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_emails = [["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]]
	expected_output = [2]
	for i in range(len(input_emails)):
		if numUniqueEmails(input_emails[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', numUniqueEmails(input_emails[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(numUniqueEmails(input_emails[-1]))
	

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