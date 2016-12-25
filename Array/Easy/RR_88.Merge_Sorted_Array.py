#========== Backwards ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
            
#============ Backwards more clear ===========
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1_idx = m - 1
        nums2_idx = n - 1
        union = m + n - 1
        while nums1_idx >= 0 and nums2_idx >= 0:
            if nums1[nums1_idx] > nums2[nums2_idx]:
                nums1[union] = nums1[nums1_idx]
                union -= 1
                nums1_idx -= 1
            else:
                nums1[union] = nums2[nums2_idx]
                union -= 1
                nums2_idx -= 1
        while nums2_idx >= 0:
            nums1[union] = nums2[nums2_idx]
            union -= 1
            nums2_idx -= 1
