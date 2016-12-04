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
            
        
