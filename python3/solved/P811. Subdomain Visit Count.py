# ToDo:

"""
811. Subdomain Visit Count
Easy

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Notes:

    The length of cpdomains will not exceed 100. 
    The length of each domain name will not exceed 100.
    Each address will have either 1 or 2 "." characters.
    The input count in any count-paired domain will not exceed 10000.
    The answer output can be returned in any order.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
## test part
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        cpdomains: List[str]
        rtype: List[str]
        """
        
## code here
#1
class Solution:
    def subdomainVisits(self, cpdomains):
        domain_cp = {}
        subdomains = set()
        for cpdomain in cpdomains:
            cp, domain = cpdomain.split(' ')
            domain_cp[domain] = int(cp)

            sub = domain.split('.')
            for i in range(len(sub)):
                subdomains.add(sub[i:])


#1.1
"""
Success
Runtime: 52 ms, faster than 73.33% of Python3 online submissions for Subdomain Visit Count.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Subdomain Visit Count.
"""
class Solution:
    def subdomainVisits(self, cpdomains):
        subdomains_cp = {}
        for cp_domain in cpdomains:
            cp, domain = cp_domain.split(' ')
            cp = int(cp)
            sub = domain.split('.')
            for i in range(len(sub)):
                subdomain = '.'.join(sub[i:])
                if subdomain not in subdomains_cp:
                    subdomains_cp[subdomain] = cp
                else: subdomains_cp[subdomain] += cp
        res = []
        for subdomain, cp in subdomains_cp.items():
            res.append(''.join([str(cp), ' ', subdomain]))
        return res


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [["9001 discuss.leetcode.com"], ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]]
    expected_output = [["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"], ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]]
    for i in range(len(input1)):
        if subdomainVisits(input1[i]) != expected_output[i]:
            print("Wrong!!!", ' Output:', subdomainVisits(input1[i]), '; Expected Output:', expected_output[i])
        else:
            print("Right")
    # print(subdomainVisits(input1[-1]))
    

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