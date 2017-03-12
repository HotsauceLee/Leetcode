# =========== Math ===============
# Time: O(1)
# Space: O(1)
# Idea: if I can leave 4 to my opponent, I will win.
#    so if I move first and I have n%4 != 0 stones, 
#    I can always try to leave for to him.
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n%4 == 0 else True
