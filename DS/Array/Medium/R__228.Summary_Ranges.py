# ========= compare with the last one =========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lens = len(nums)
        if not lens: return []
        result = [str(nums[0])]
        for i in xrange(1, lens):
            if nums[i] - nums[i - 1] == 1:
                # when in order, won't do anything unless we are
                # in the last one
                if i == len(nums) - 1:
                   result[-1] += '->%s'%nums[i]
            else:
                # Won't add the last one unless last one is not
                # the only one
                if int(result[-1]) != nums[i - 1]:
                   result[-1] += '->%s'%nums[i - 1] 
                result.append(str(nums[i]))
            
            last = nums[i]
        return result
        
# ========= Put a whole range at a time =========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        idx = 0
        result = []
        while idx < len(nums):
            cur = nums[idx]
            while idx + 1 < len(nums) and nums[idx + 1] - nums[idx] == 1:
                idx += 1
            if cur != nums[idx]:
                result.append('%s->%s'%(cur, nums[idx]))
            else:
                result.append(str(cur))
            idx += 1
        return result
