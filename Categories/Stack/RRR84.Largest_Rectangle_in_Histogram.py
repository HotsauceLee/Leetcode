"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""

# ============== Increasing Stack ===============
# Time: O(2n)
# Space: O(n)
# Idea: find the first smaller one of each one's left and right
"""
use stack to maintain the prev first smaller one.
when encounter one that is smaller than the last one in stack,
pop out all the ones that are bigger than the current one, while
calculating the area of each popped one.
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        heights += [0]
        stack, result = [], 0
        for i in xrange(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                last = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                result = max(result, width*heights[last])

            stack.append(i)

        return result
