#============ Boyer–Moore majority vote algorithm ==========
# Time: O(n)
# Space: O(1)
# NOTE: majority must exist!
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for i in nums[1:]:
            if not count:
                majority = i
                count = 1
            elif i == majority: count += 1
            else:count -= 1
                        
        return majority

#============== Dict ===============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        d = {nums[0]: 1}
        for i in nums[1:]:
            if not d.has_key(i):
                d[i] = 1
            else:
                d[i] += 1
                if d[i] > d[majority]:
                    majority = i
                        
        return majority

#============== Sort =================
# Time: O(log(n))
# Space: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]

# ========== Divide and concur =========
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        if len(nums) == 1: return nums[0]
        
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b: return a
        return [a, b][nums.count(b) > len(nums)//2]

# =========== Random ============
from random import randrange

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            idx = randrange(len(nums))
            val = nums[idx]
            if nums.count(val) > len(nums)//2: return val
