# =========== Use array value as index(changed array value, not allowed!) =============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        for i in xrange(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                return abs(nums[i])
            nums[idx] = -nums[idx]

# =========== Binary search ==============:
# Time: O(nlog(n))
# Space: O(1)
