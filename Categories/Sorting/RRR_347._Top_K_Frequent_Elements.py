"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# ============= bucket sort =============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        bucket = [None]*(len_nums + 1)
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        # print d
        for key in d.keys():
            freq = d[key]
            if not bucket[freq]:
                bucket[freq] = [key]
            else:
                bucket[freq].append(key)
        
        result = []
        # print bucket
        for b in bucket[::-1]:
            if not b:
                continue

            result += b
            if len(result) >= k:
                result = result[:k]
                break
            
        return result
            
        
