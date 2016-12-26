#======== slow and fast pointer =========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lid = 0
        for n in nums:
            if n != val:
                nums[lid] = n
                lid += 1
            
        return lid
