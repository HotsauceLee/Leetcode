# ============ keep max =============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        max_result = 0
        cur_len = 0
        for n in nums:
            if n == 1:
                cur_len += 1
                max_result = max(max_result, cur_len)
            else:
                cur_len = 0
                
        return max_result
