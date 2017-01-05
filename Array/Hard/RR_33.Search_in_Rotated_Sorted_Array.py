class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target: return mid
            # Larger zone. Floor divison leans toward left, so add equals here.
            if nums[mid] >= nums[left]:
                # Target in the larger zone?
                if nums[left] <= target < nums[mid]:
                    # Go to larger zone
                    right = mid - 1
                else:
                    # Go to right half
                    left = mid + 1
            # Smaller zone.
            else:
                # Target in the smaller zone? If target == nums[mid],
                # we won't be here, so add equals to the right.
                if nums[mid] < target <= nums[right]:
                    # Go to smaller zone
                    left = mid + 1
                else:
                    # go to the other half
                    right = mid - 1
            
        # Didn't find match
        return -1
