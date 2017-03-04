# ============= Magic =============
# Time: O(2n)
# Space: O(1)
# Idea:
"""
The first loop is to find the candidate as the author explains. In detail, suppose the candidate after the first for loop is person k, it means 0 to k-1 cannot be the celebrity, because they know a previous or current candidate. Also, since k knows no one between k+1 and n-1, k+1 to n-1 can not be the celebrity either. Therefore, k is the only possible celebrity, if there exists one.

The remaining job is to check if k indeed does not know any other persons and all other persons know k.
"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in xrange(1, n):
            if knows(candidate, i):
                candidate = i
                
        for i in xrange(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
                
        return candidate
