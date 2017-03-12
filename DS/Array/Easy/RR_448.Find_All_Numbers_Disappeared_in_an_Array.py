# =========== Set to negative ============
# Time: O(2n)
# Space: O(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
            i += 1
        
        result = [] 
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                result.append(i + 1)
            i += 1
                
        return result
