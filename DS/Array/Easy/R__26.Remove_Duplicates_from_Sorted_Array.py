#========== slow and fast pointers ===========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        slow = fast = 1
        while slow < lens and fast < lens:
            while fast < lens and nums[fast] == nums[fast - 1]:
                fast += 1
            if fast >= lens: break
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
            
        return slow if lens >= 2 else lens
        
#========== one pointers ===========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)
        lid = 1
        for i in xrange(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[lid] = nums[i]
                lid += 1
        return lid
