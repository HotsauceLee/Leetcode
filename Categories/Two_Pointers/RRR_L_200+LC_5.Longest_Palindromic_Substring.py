"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

# ============== Expend from every element and in between ==============
# Time: O(n^2)
# Space: O(1)
"""
I think you can look at it at this way. If len is even number and center would not point to any char at the string. So at this moment i will point to the char at the left side of the center. For example,
a b b a
i
center is between the 2 b, and i, in order to reach left 'a', cannot walk the same distances as would it do to reach right side 'a'. So it cannot be start = i - len / 2;
but why not i - len / 2 -1 instead of i - (len - 1) / 2?
I think this is because there will condition when len is odd number, such as
a b c b a
i
At this time i is pointing to the center char, and distances being walked to left and right should be the same.
Please not that java is integer division, such that if n is odd, then n / 2 == (n - 1) / 2.
so start = i - (len - 1) / 2 is just getting rid of that useless remainder(I mean at this scenario) out.
This is my understanding, plz if my logic is wrong, point it out for me thx!
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        
        start = end = 0
        for i in xrange(len(s)):
            len_from_self = self.__expend(s, i, i)
            len_from_sides = self.__expend(s, i, i + 1)
            cur_len = max(len_from_self, len_from_sides)
            if cur_len > end - start:
                # if cur_len is an even number, then left side
                # is shorter since is started from i and i+1
                # if it is an odd number, then 
                # cur_len/2 = (cur_len - 1)/2
                start = i - (cur_len - 1)/2
                # right side will always be the same
                end = i + cur_len/2
            print start ,end
                
        return s[start:end+1]

    def __expend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
        
