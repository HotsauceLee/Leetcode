#============= Dict =============
# Time: O(n^2)
# Space: O(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for idx, n in enumerate(nums):
            if not d.has_key(n):
                d[n] = [idx]
            else:
                for i in d[n]:
                    if abs(i - idx) <= k:
                        return True
                d[n].append(idx)
                
        return False
        
#============= Dict only compare with latest idx =============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for idx, n in enumerate(nums):
            if d.has_key(n) and abs(d[n] - idx) <= k: return True
            d[n] = idx

        return False
        
