# ============= Use value as index =============
# Time: O(2n)
# Space: O(1)
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            pos = abs(nums[i])
            target_idx = pos - len(nums) - 1 if pos > len(nums) else pos - 1
            if nums[target_idx] > 0:
                nums[target_idx] = -nums[target_idx]
            else:
                nums[target_idx] = nums[target_idx] - len(nums)
                
        result = []
        for idx, n in enumerate(nums):
            if abs(n) > len(nums):
                result.append(idx + 1)
                
        return result
        
# ============= One pass ================
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(nums)):
            target_idx = abs(nums[i]) - 1
            if nums[target_idx] < 0:
                result.append(target_idx + 1)
            nums[target_idx] = -nums[target_idx]
                
        return result
