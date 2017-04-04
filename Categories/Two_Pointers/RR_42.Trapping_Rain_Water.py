"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

# ============ Two Pointers ==============
# Time: O(n)
# Space: O(1)
# Idea:
"""
Fill in water from the lower end. if cur_left/cur_right > max_left, max_right, update max.
otherwise add in cur_water
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        max_left = max_right = 0
        left, right = 0, len(height) - 1
        max_water = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    max_water += max_left - height[left]
                    
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    max_water += max_right - height[right]
                    
                right -= 1
                
        return max_water
