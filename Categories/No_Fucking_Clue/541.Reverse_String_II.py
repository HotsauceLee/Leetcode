"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
Show Company Tags
Show Tags
Show Similar Problems

"""

# ================ counter =================
# Time: O(n)
# Space: O(k)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k <= 1 or not s:
            return s

        counter = k
        reversing = True
        tmp = ""
        result = ""
        for c in s:
            if counter == 0:
                result += tmp
                tmp = ""
                reversing = False
            if counter == k:
                reversing = True

            if reversing:
                tmp = c + tmp
                counter -= 1
            else:
                result += c
                counter += 1
                
        if tmp:
            result += tmp
        return result
                
                
                
        
