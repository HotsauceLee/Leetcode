# ======== Back tracking =============
# Time: ?
# Space: ?
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, begin, cur_sum, cur_path, result):
            if len(cur_path) == 3:
                if cur_sum == 0:
                    result.append(cur_path[:])
                return
                    
            for i in xrange(begin, len(nums)):
                if i > begin and nums[i] == nums[i-1]: continue
                cur_sum += nums[i]
                cur_path.append(nums[i])
                helper(nums, i + 1, cur_sum, cur_path, result)
                cur_path.pop()
                cur_sum -= nums[i]
                
        nums.sort()
        result = []
        helper(nums, 0, 0, [], result)
        return result
        
# ========== Sort + Binary search ===========
# Time: sort - nlog(n), BS- log(n), outer loop - n, inner loop - n*logn + (n-1)*log(n-1) + ...
#   O(nlog(n) + logn*n^2) NOT SURE!!!
# Space: O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def binary_search(begin, end, target):
            while begin <= end:
                mid = (begin + end)//2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    begin = mid + 1
                else:
                    return True
            return False
        
        nums.sort()
        result = []   
        for outer in xrange(len(nums)):
            if outer > 0 and nums[outer] == nums[outer-1]: continue
            for inner in xrange(outer + 1, len(nums)):
                if inner > outer + 1 and nums[inner] == nums[inner-1]: continue
                diff = 0 - nums[inner] - nums[outer]
                if diff > nums[-1] or inner + 1 >= len(nums) or diff < nums[inner + 1]: continue
                if binary_search(inner + 1, len(nums) - 1, diff):
                    result.append([nums[outer], nums[inner], diff])
                    
        return result

#=============== loop + 2sum ==============
# Time: O(nlog(n) + n^2)
# Space: O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            target = 0 - nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                cur_val = nums[lo] + nums[hi]
                if cur_val > target: hi -= 1
                elif cur_val < target: lo += 1
                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                    lo += 1
                    hi -= 1
                
        return result


