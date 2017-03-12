# ========= 3 sum + extra loop ==========
# Time: O(nlog(n) + n^3)
# Space: O(1)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in xrange(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                t = target - nums[i] - nums[j]
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    cur_val = nums[lo] + nums[hi]
                    if cur_val > t: hi -= 1
                    elif cur_val < t: lo += 1
                    else:
                        result.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1
                
        return result
        
# ============ back tracking + 2sum ============
# Time: ?
# Space: ?
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(nums, begin, cur_sum, cur_path, result):
            if 4 - len(cur_path) > 2:
                for i in xrange(begin, len(nums)):
                    if i > begin and nums[i] == nums[i-1]: continue
                    cur_sum += nums[i]
                    cur_path.append(nums[i])
                    helper(nums, i + 1, cur_sum, cur_path, result)
                    cur_path.pop()
                    cur_sum -= nums[i]
            else:
                if begin >= len(nums): return
                t = target - cur_sum
                lo, hi = begin, len(nums) - 1
                while lo < hi:
                    cur_val = nums[lo] + nums[hi]
                    if cur_val < t: lo += 1
                    elif cur_val > t: hi -= 1
                    else:
                        result.append(cur_path[:] + [nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1
                
        nums.sort()
        result = []
        helper(nums, 0, 0, [], result)
        return result
        
#============ same with smart breaks ============
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
