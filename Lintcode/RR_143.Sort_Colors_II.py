"""
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

 Notice

You are not suppose to use the library's sort function for this problem.

k <= n

Have you met this question in a real interview? Yes
Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
"""
# ============== binary Search divide to two groups at a time ==============
# Time: O(nlog(n))
# Space: O(1)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or len(colors) < 2:
            return
        
        self.rainbow(0, len(colors) - 1, 1, k, colors)
        
    def rainbow(self, left, right, color_left, color_right, colors):
        if color_left >= color_right or left > right:
            return

        color_mid = (color_left + color_right)/2
        l, r = left, right
        while left <= right:
            # color mid leans toward left, if >= color_mid couldn't seperate two adjacent colors.
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1
                
            if left > right:
                break
            
            colors[left], colors[right] = colors[right], colors[left]
            left += 1
            right -= 1
        
        self.rainbow(l, right, color_left, color_mid, colors)
        self.rainbow(left, r, color_mid + 1, color_right, colors)
