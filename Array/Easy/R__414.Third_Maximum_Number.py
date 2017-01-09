#============ 3 pointers ===============
# Time: O(3n)
# Space: O(1)
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float('-inf')
        for n in nums:
            if n in [first, second, third]:
                continue
            
            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n
                
        return first if third == float('-inf') else third

# ============= Python set + maxium ==============
# Time: O(4n)
# Space: O(1)
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
