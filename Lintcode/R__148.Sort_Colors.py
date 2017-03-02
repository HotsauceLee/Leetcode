# ========== 3 pointers grouping ========
# Time: O(n)
# Space: O(1)
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return
        
        left, right, begin = 0, len(nums) - 1, 0
        while begin <= right:
            if nums[begin] == 0:
                nums[begin], nums[left] = nums[left], nums[begin]
                left += 1
                begin += 1
            elif nums[begin] == 2:
                nums[begin], nums[right] = nums[right], nums[begin]
                right -= 1
            else:
                begin += 1
