#============= Flip p max and n min =============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        
        all_max = p_max = n_min = 0
        for n in nums:
            if n < 0:
                p_max, n_min = n_min, p_max
            p_max = max(p_max*n, n)
            n_min = min(n_min*n, n)
            all_max = max(all_max, p_max)
            
        return all_max
