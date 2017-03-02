# ============= Custom Comparator =============
# Time: O(nlog(n) + n)
# Space: O(n)
class Node(object):
    def __init__(self, index=None, sum=None):
        self.index = index
        self.sum   = sum
        
    def __cmp__(self, other):
        return self.sum - other.sum

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []
        if len(nums) <= 1:
            return [0, 0]
            
        sum_array = [Node(-1, 0)]
        for i in xrange(len(nums)):
            sum_so_far = nums[i] + sum_array[-1].sum
            sum_array.append(Node(i, sum_so_far))
            
        sum_array.sort()
        
        result = []
        min_sub = float('inf')
        for i in xrange(1, len(sum_array)):
            cur_sub = abs(sum_array[i].sum - sum_array[i - 1].sum)
            if cur_sub < min_sub:
                min_sub = cur_sub
                if sum_array[i].index < sum_array[i - 1].index:
                    result = [sum_array[i].index + 1, sum_array[i - 1].index]
                else:
                    result = [sum_array[i - 1].index + 1, sum_array[i].index]
                    
        return result
