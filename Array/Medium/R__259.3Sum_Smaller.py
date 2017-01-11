# =========== Sort + Loops ==============
# Time: O(nlog(n)+n^3)
# Space: O(1)
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in xrange(len(nums) - 2):
            for j in xrange(i + 1, len(nums) - 1):
                diff = target - nums[i] - nums[j]
                k = j + 1
                while k < len(nums) and nums[k] < diff:
                    result += 1
                    k += 1
                        
        return result

# =========== Sort + Binary search ============
# Time: O(nlog(n) + n^2)
# Space: O(1)
# Idea: When binary searching, if left + right < diff,
#       left + (right-1), left + (right-2)... must < diff
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in xrange(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
                        
        return result
