"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""

# ============== keep adding to existing results ==============
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        tmp, has = [], set()
        for n in nums:
            tmp.append([n])
            len_save = len(tmp)
            for t in tmp[:len_save - 1]:
                if n >= t[-1]:
                    if str(t + [n]) not in has:
                        tmp.append(t[:] + [n])
                        has.add(str(t + [n]))
                    
        return [t for t in tmp if len(t) >= 2]
