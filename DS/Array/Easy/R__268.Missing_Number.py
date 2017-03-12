# ============= Add one to the end ===================
# Time: O(2n)
# Space: O(1)
class Solution(object):
    def missingNumber(self, nums):
        if not nums:
            return None

        nums += [len(nums)+1]
        for npo in nums[:-1]:
            nums[abs(npo)] = -nums[abs(npo)]

        zero = None
        for idx, n in enumerate(nums):
            if n == 0:
                zero = idx 
                continue
            if n > 0:
                return idx 

        return zero
        
# ============= XOR ==================
# Time: O(n)
# Spcee: O(1)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums += [0] 
        result = 0 
        for idx, val in enumerate(nums):
            result = result ^ idx ^ val 

        return result
    
# ============= sum ================
# Time: O(n)
# Space: O(1)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        real_sum = len(nums)*(len(nums)+1)/2
        for n in nums:
            real_sum -= n

        return real_sum
    
# ============= Binary Search ===============
# Time: O(nlog(n) + log(n))
# Space: O(1)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)/2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1

        return left
