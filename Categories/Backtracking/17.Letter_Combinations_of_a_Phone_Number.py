"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

# ==================== DFS ==================
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

        def dfs(cur_str, cur_idx, result):
            if cur_idx == len(digits):
                result.append(cur_str)
                return
                
            cur_digit = int(digits[cur_idx])
            for l in d[cur_digit]:
                cur_str += l
                dfs(cur_str, cur_idx + 1, result)
                cur_str = cur_str[:-1]
        
        result = []
        dfs("", 0, result)
        return result
