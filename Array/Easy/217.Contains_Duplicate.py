#=========== Dict ============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if d.has_key(n):
                return True
            else:
                d[n] = n
      
        return False
#============ Sort ==========
# Time: O(nlog(n) + n)
# Space: O(1)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                return True
            i += 1
                
        return False
        
# =========== Set =============
# Time: ?
# Space: ?
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
