#================== Dict =====================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for idx, val in enumerate(nums):
            if dict.has_key(val):
                if val + val == target:
                    return [idx, dict[val]] if idx < dict[val] else [dict[val], idx]
                else:
                    continue
            
            dict[val] = idx
            if dict.has_key(target - val):
                if idx == dict[target - val]:
                    continue
                return [idx, dict[target - val]] if idx < dict[target - val] else [dict[target - val], idx]
                
        return None
