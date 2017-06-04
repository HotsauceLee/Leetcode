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
            # define & change current state
            if counter == 0:
                result += tmp
                tmp = ""
                reversing = False
            if counter == k:
                reversing = True
            
            # do things base on current state
            if reversing:
                tmp = c + tmp
                counter -= 1
            else:
                result += c
                counter += 1
                
        result += tmp
        return result
                
# ================ Swap ================
# Time: O( < n)
# Space: O(n)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k <= 1 or not s:
            return s
            
        s_list = list(s)
        for i in xrange(0, len(s), 2*k):
            j = min(i + k - 1, len(s) - 1)
            self.swap(s_list, i, j)
            
        return ''.join(s_list)
        
    def swap(self, char_list, begin, end):
        while begin < end:
            char_list[begin], char_list[end] = char_list[end], char_list[begin]
            begin += 1
            end -= 1
        
                
        
                
                
                
        
