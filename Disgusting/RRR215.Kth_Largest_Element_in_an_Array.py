# =========== Quick sort. only do one side ===========
# Time: best O(nlog(n)), worst O(n^2)
# Space: O(1)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            smaller = self.__partition(nums, lo, hi)
            if smaller == k:
                return nums[k]
            if smaller < k:
                lo = smaller + 1
            else:
                hi = smaller - 1
        
        # when len(nums) == 1 or lo and hi meets.
        # Doesn't matter lo or hi
        return nums[lo]
                
    def __partition(self, nums, lo, hi):
        begin, end = lo, hi
        while begin < end:
            # move first, then check
            while begin <= hi and nums[begin] <= nums[lo]:
                begin += 1
            while end >= lo and nums[end] > nums[lo]:
                end -= 1
                
            if begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
        
        # end always ends up in the last one of smaller or equals.
        nums[lo], nums[end] = nums[end], nums[lo]
        return end
