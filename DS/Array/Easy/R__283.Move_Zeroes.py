# ============= Push back non-zero ===========
# Time: O(2n)
# Space: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tracker = 0
        for n in nums:
            if n != 0:
                nums[tracker] = n
                tracker += 1
                
        while tracker < len(nums):
            nums[tracker] = 0
            tracker += 1
            
# =========== Swap =================
# Time: O(n)
# Space: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
