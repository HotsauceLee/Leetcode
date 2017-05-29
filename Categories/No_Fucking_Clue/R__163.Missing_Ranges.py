"""
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""

# ============ loop ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            return ["%s->%s" % (lower, upper)]
        
        result = []
        if nums[0] > lower:
            if nums[0] - lower == 1:
                result.append(str(lower))
            else:
                result.append("%s->%s" % (lower, nums[0] - 1))
            prev = nums[0]
        else:
            prev = lower

        for n in nums:
            if n - prev >= 2:
                if n - prev == 2:
                    result.append(str(n-1))
                else:
                    result.append("%s->%s" % (prev + 1, n - 1))
            prev = n
            
        if prev < upper:
            if upper - prev == 1:
                result.append(str(upper))
            else:
                result.append("%s->%s" % (prev + 1, upper))
            
        return result
            
            
# ============ Shorter ===============
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        prev = lower - 1
        for i in xrange(len(nums) + 1):
            n = nums[i] if i < len(nums) else upper + 1
            # here is why set prev = lower - 1 and 
            # n = upper + 1 when i == len(nums)
            # if lower and nums[0] diffs by 1, we only want to
            # put lower in, so n - prev = 2 and n - 1 goes in
            # if they diff more than 1, the 1 will be added back
            # in elif n - prev > 2:
            # same when i == len(nums), both senario will take out
            # the extra 1.
            # normal case just put 1 in and a range when diff more than 2.
            if n - prev == 2:
                result.append(str(n-1))
            elif n - prev > 2:
                result.append("%s->%s" % (prev + 1, n - 1))
            prev = n
            
        return result
            
            
