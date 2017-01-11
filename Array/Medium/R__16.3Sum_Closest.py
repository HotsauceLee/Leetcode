# ========= Sort + Binary search ============
# Time: O(nlog(n) + n^2)
# Space: O(1)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = float('inf')
        for i in xrange(len(nums) - 2):
            diff = target - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                # This saves a lot of time
                if cur_sum == target: return cur_sum
                
                if abs(cur_sum - target) < abs(result - target):
                    result = nums[i] + nums[left] + nums[right]
                    
                if nums[left] + nums[right] > diff:
                    right -= 1
                else:
                    left += 1
                
        return result
