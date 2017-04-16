"""
Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

 Notice

You do not care about the accuracy of the result, we will help you to output results.

Have you met this question in a real interview? Yes
Example
Given n = 2 return 1.41421356
"""

# =============== BS ===============
# Time: O(log(x))
# Space: O(1)
# Trap: need a min precision, or it will never end
#   also, if the question requires -8, set it bigger
#   than -8 so that it could round up to the result.
"""
// 二分浮点数 和二分整数不同
            // 一般都有一个精度的要求 譬如这题就是要求小数点后八位
            // 也就是只要我们二分的结果达到了这个精度的要求就可以
            // 所以 需要让 right 和 left 小于一个我们事先设定好的精度值 eps
            // 一般eps的设定1e-8,因为这题的要求是到1e-8,所以我把精度调到了1e-12
            // 最后 选择 left 或 right 作为一个结果即可 
"""
class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        # Write your code here
        if x <= 0:
            return x
            
        left = 0.0
        right = x
        eps = 1e-12
        
        # When x < 1, it's sqrt is bigger than itself
        # if we set right to it, mid*mid will be
        # smaller and smaller than x and the result will
        # always be x itself. Set right to 1 so that left
        # could pass x and find the mid that is bigger
        # than x.
        if right < 1:
            right = 1.0
            
        while (right - left) > eps:
            mid = (left + right)/2
            cur_square = mid*mid
            if cur_square < x:
                left = mid
            else:
                right = mid
                
        return left
        
