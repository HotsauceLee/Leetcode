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

# ======= Bit ================

# ========== Divide and concur =========

# =========== Random ============
