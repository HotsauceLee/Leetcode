"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

# =========== two pointers ===============
# Time: O(n)
# Space: O(1)
public class Solution {
    public int trap(int[] height) {
        if ( height == null || height.length == 0 ) {
            return 0;
        }
        
        int left = 0;
        int right = height.length - 1;
        int leftMax = Integer.MIN_VALUE;
        int rightMax = Integer.MIN_VALUE;
        int result = 0;
        while ( left < right ) {
            if ( height[left] > height[right] ) {
                if ( height[right] < rightMax ) {
                    result += rightMax - height[right];
                } else {
                    rightMax = height[right];
                }
                
                right--;
            } else {
                if ( height[left] < leftMax ) {
                    result += leftMax - height[left];
                } else {
                    leftMax = height[left];
                }
                
                left++;
            }
        }
        
        return result;
    }
}
