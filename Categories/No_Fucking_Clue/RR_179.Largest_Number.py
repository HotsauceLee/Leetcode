"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

# ============== string comparator ==============
# Time: O(nlog(n) + n)
# Space: O(1)
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ""
            
        def my_cmp(n1, n2):
            case1 = str(n1) + str(n2)
            case2 = str(n2) + str(n1)
            if case1 > case2:
                return -1
            elif case1 < case2:
                return 1
            return 0
        
        # O(nlog(n))
        nums.sort(cmp=my_cmp)
        result = ""
        # O(n)
        for n in nums:
            result += str(n)
            
        return result if result[0] != '0' else '0'
