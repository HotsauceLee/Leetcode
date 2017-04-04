"""
Indeed this question can be solved in one pass and O(1) space, but it's probably hard to come up with in a short interview. If you have read the stack O(n) solution for Largest Rectangle in Histogram, you will find this solution is very very similar.

The main idea is : if we want to find out how much water on a bar(bot), we need to find out the left larger bar's index (il), and right larger bar's index(ir), so that the water is (min(A[il],A[ir])-A[bot])*(ir-il-1), use min since only the lower boundary can hold water, and we also need to handle the edge case that there is no il.

To implement this we use a stack that store the indices with decreasing bar height, once we find a bar who's height is larger, then let the top of the stack be bot, the cur bar is ir, and the previous bar is il.
"""

# ============= Stack ==============
# Time: O(2n)
# Space: O(n)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        stack = []
        i = 0
        max_water = 0
        while i < len(height):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bottom = stack.pop()
                cur_water = 0 if not stack else (min(height[stack[-1]], height[i]) - height[bottom])*(i - stack[-1] - 1)
                max_water += cur_water

        return max_water
