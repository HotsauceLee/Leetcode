"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

# ================= binary search ==================
# Time: O(m*log(n))
# Space: O(1)
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
            
        nums2.sort()
        result = set()
        for n in nums1:
            if self.bs(nums2, n):
                result.add(n)
                
        return list(result)
        
    def bs(self, nums, n):
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end)/2
            if nums[mid] == n:
                return True
                
            if nums[mid] < n:
                begin = mid + 1
            else:
                end = mid - 1
                
        return False
