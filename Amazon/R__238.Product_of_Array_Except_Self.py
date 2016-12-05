# ============== Division =================
# Time: O(n)
# Space: O(1) Not counting result list
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return nums
        product_all = 1
        zero = 0
        result = [0]*len(nums)
        for i in nums:
            if i != 0:
                product_all *= i
                continue
            zero += 1
                
        if zero > 1:
            return result
        
        if zero == 1:
            idx = nums.index(0)
            result[idx] = product_all
            return result
        
        for idx, val in enumerate(nums):
                result[idx] = product_all/val
                
        return result
            
# ============== Two passes =================
# Time: O(n)
# Space: O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lens = len(nums)
        result = [1]*lens
        cur_prod = nums[0]
        for i in range(1, lens):
           result[i] = cur_prod
           cur_prod *= nums[i]
            
        cur_prod = nums[lens - 1]
        i = lens - 2
        while i >= 0:
            result[i] *= cur_prod
            cur_prod *= nums[i]
            i -= 1
            
        return result
