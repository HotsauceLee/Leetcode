# ============== Magic ===============
# Time: O(n)
# Space: O(1)
# Idea:
"""
https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return
        
        # 1. Find the first decending number fron right to left
        i = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1
        found = False
        chosen_idx = None
        decending_begin = i
        if i != 0:
            found = True
            chosen_idx = i - 1

        if found:
            # 2. Find the first number larger than chosen number, from right to left
            i = len(nums) - 1
            while i >= 0 and nums[i] <= nums[chosen_idx]:
                i -= 1
            first_larger = i
            
            # 3. swap them out
            nums[chosen_idx], nums[first_larger] = nums[first_larger], nums[chosen_idx]
            
        # 4. reverse everything from the beginning of reverse
        begin, end = decending_begin, len(nums) - 1
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1
                
        
            
