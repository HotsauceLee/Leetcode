"""
Given two rectangles, find if the given two rectangles overlap or not.

 Notice

l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

l1 != r2 and l2 != r2

Have you met this question in a real interview? Yes
Example
Given l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], return true

Given l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], return `false
"""

# ============= Think reverse - when do they not overlap ==============
# Time: O(1)
# Space: O(1)
# Trap: too many senarios when they overlay, then reversely
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point} l1 top-left coordinate of first rectangle
    # @param {Point} r1 bottom-right coordinate of first rectangle
    # @param {Point} l2 top-left coordinate of second rectangle
    # @param {Point} r2 bottom-right coordinate of second rectangle
    # @return {boolean} true if they are overlap or false
    def doOverlap(self, l1, r1, l2, r2):
        # Write your code here
        max_x1, min_x1, max_y1, min_y1 = r1.x, l1.x, l1.y, r1.y
        max_x2, min_x2, max_y2, min_y2 = r2.x, l2.x, l2.y, r2.y

        x_overlap = not (( max_x2 > min_x1 and min_x2 > max_x1 ) or ( max_x1 > min_x2 and min_x1 > max_x2 ))
        y_overlap = not (( max_y2 > min_y1 and min_y2 > max_y1 ) or ( max_y1 > min_y2 and min_y1 > max_y2 ))
        
        return x_overlap and y_overlap
