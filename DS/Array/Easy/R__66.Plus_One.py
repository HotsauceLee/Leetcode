# ============ Stop at digit < 9 ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        while idx >= 0:
            if digits[idx] < 9:
                digits[idx] += 1
                return digits
            digits[idx] = 0
            idx -= 1
        
        result = [0]*(len(digits) + 1)
        result[0] = 1
        return result
