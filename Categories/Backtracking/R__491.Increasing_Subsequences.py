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

# =============== backtracking ===============
# Time: O()
# Space: O()
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
            
        def dfs(prev, seq_so_far, cur_idx, result, has):
            for i in xrange(cur_idx, len(nums)):
                cur = nums[i]
                if cur >= prev:
                    seq_so_far.append(cur)
                    if len(seq_so_far) >= 2 and str(seq_so_far) not in has:
                        has.add(str(seq_so_far))
                        result.append(seq_so_far[:])
                    dfs(cur, seq_so_far, i + 1, result, has)
                    seq_so_far.pop()
                    
        result = []
        has = set()
        dfs(float('-inf'), [], 0, result, has)
        return result
                
                    
