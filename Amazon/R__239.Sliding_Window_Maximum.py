from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k): 
        """ 
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        if not nums: return result
        lens = len(nums)
        q = deque()
        
        for i in range(lens):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if i < k - 1:
                continue

            while len(q) and q[0] < i - k + 1:
                q.popleft()
            result.append(nums[q[0]])

        return result
        
