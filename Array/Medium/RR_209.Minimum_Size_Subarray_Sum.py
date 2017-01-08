#========== Slow and fast pointers =============
# Time: O(2n)
# Space: O(1)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, cur_sum, min_dist = 0, 0, 0, float('inf')
        while fast < len(nums):
            cur_sum += nums[fast]
            fast += 1
            while cur_sum >= s:
                min_dist = min(min_dist, fast - slow)
                cur_sum -= nums[slow]
                slow += 1
                
        return 0 if min_dist == float('inf') else min_dist
        
# ============ Binary serach =============
# Time: O(nlog(n))
# Space: O(1)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def window_exist(size):
            window_sum = 0
            for i in xrange(len(nums)):
                window_sum += nums[i]
                # maintain window size
                if i >= size:
                    window_sum -= nums[i-size]
                if window_sum >= s:
                    return True
            return False
        
        # Binary search on window size, not 
        begin, end, min_window = 1, len(nums), 0
        while begin <= end:
            mid = (begin+end)//2
            if window_exist(mid):
                end = mid - 1
                min_window = mid
            else:
                begin = mid + 1
                
        return min_window
