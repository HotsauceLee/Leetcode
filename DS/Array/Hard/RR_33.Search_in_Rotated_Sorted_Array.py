# ============= Binary search ================
# Time: O(log(n))
# Space: O(1)
# Idea:
"""
[__larger__|_____smaller_____]
If target in the larger zone, go left. otherwise, go right.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        Corner cases:
        1. [0] 0
        2. [0] 1
        3. [1,2] 2
        4. [2,1] 1
        5. [4,5,6,7,0,1,2] 5
        6. [4,5,6,7,0,1,2] 1
        
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target: return mid
            # Larger zone. Floor divison leans toward left, so add equals here.
            # case [2,1] 1
            if nums[mid] >= nums[left]:
                # Target in the smaller zone? If target == nums[mid],
                # we won't be here, so add equals to the left.
                # Also make sense to think that we have to include the
                # whole range inclusively
                if nums[left] <= target < nums[mid]:
                    # Go to larger zone
                    right = mid - 1
                else:
                    # Go to right half
                    left = mid + 1
            # Smaller zone.
            # Case [5,1,3] 3
            else:
                # Target in the larger zone?
                # Also make sense to think that we have to include the
                # whole range inclusively, so add equals to the left end.
                if nums[mid] < target <= nums[right]:
                    # Go to smaller zone
                    left = mid + 1
                else:
                    # go to the other half
                    right = mid - 1
            
        # Didn't find match
        return -1
