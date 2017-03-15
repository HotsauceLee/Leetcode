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
            # when cur_sum < s, prev has already passed valid range,
            # but if we keep it at the last valid point, when plusing
            # the next one, it must still be valid, better off go one
            # step further let cur_sum build up again then start taking
            # prev off.

            # In another way, if we keep the last valid point, if after plusing the next one still valid after minusing prev, it updates max twice. If we dont keep theast valid, it will update once
            while cur_sum >= s:
                # reason why fast - slow instead of fast - slow + 1
                # is because fast already += 1 up there
                # better: for fast in xrange(len(nums)) and use
                # fast - slow + 1
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
        
        # Binary search on window size, not array values
        begin, end, min_window = 1, len(nums), 0
        while begin <= end:
            mid = (begin+end)//2
            if window_exist(mid):
                end = mid - 1
                min_window = mid
            else:
                begin = mid + 1
                
        return min_window
