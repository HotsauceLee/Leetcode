# =========== Binary search ==============:
# Time: O(nlog(n))
# Space: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        lens = len(nums)
        if lens <= 1:
            return 0
            
        begin, end = 1, lens - 1
        while begin < end:
            mid = (begin + end)/2
            count = self.count_less_or_equal(mid, nums)
            
            if count <= mid:
                begin = mid + 1
            else:
                end = mid
                
        return begin
        
    def count_less_or_equal(self, target, nums):
        counter = 0
        for n in nums:
            if n <= target:
                counter += 1
                
        return counter

# =========== Find the entry point of the loop ============
# Time: O(n)
# Space: O(1)
