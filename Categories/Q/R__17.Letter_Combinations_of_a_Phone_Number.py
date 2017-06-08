"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

# =============== q ===============
# Time: O(3^n)
# Space: O(3^n)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        q = collections.deque([""])
        for idx, val in enumerate(digits):
            while len(q[-1]) == idx:
                popped = q.pop()
                for c in d[int(val)]:
                    q.appendleft(popped + c)
                    
        return list(q)
