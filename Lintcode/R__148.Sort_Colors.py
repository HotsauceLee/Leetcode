"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

 Notice

You are not suppose to use the library's sort function for this problem. 
You should do it in-place (sort numbers in the original array).

Have you met this question in a real interview? Yes
Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].
"""
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
