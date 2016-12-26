#========= Pop and insert to the beginning ========
# Time: O(k*n)
# Space: O(1)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        for i in xrange(k):
            nums.insert(0, nums.pop())
            
#========== Make a copy ==================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        nums_copy = nums[:]
        idx = 0
        while idx < lens:
            nums[(idx + k)%lens] = nums_copy[idx]
            idx += 1
 
# ============== Reverse =================
# Time: O(n): n/2 + k/2 + (n-k)/2 = n
# Space: O(1)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        lens = len(nums)
        k %= lens
        reverse(nums, 0, lens - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, lens - 1)
        
# ========== Python list index =============
# Time: ?
# Space: O(n)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        cut = len(nums) - k
        nums[:] = nums[cut:] + nums[:cut]
        
#========== Swap ==================
# Time: O(n)
# Space: O(1)
#TODO:
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        if lens <= 1: return
        k = k%lens
        if k == 0: return
    
        swap = lens - k
        i = 0
        while i < swap:
            nums[i], nums[swap] = nums[swap], nums[i]
            swap += 1
            if swap > lens - 1:
                swap = lens - k
            i += 1
