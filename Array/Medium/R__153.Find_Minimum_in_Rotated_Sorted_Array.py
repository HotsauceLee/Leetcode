#================== Binary search ==================
# Time: O(log(n))
# Space: O(1)
class Solution(object):
    def findMin(self, nums):
        """ 
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[-1]: return nums[0]
        left = 0 
        right = len(nums) - 1 
        while 1:
            mid = (left + right)//2
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                if nums[left] < nums[right]:
                    right = mid 
                else:
                    left = mid 
            elif nums[left] > nums[mid] and nums[right] > nums[mid]:
                if nums[left] < nums[right]:
                    left = mid 
                else:
                    right = mid 
            elif left == mid or right == mid:
                return nums[left] if nums[left] < nums[right] else nums[right]
            
#============ Cleaner version ==============
# Time: O(log(n))
# Space: O(1)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
                
            mid = (start+end)//2
            if nums[start] <= nums[mid]:
                start = mid+1
            else:
                end = mid
                
        return nums[start]
