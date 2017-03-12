# ============== XOR =================
# Time: O(n)
# Space: O(1)
# Idea: XOR nutrulize same values.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # XOR faster
        result = 0
        for i in nums:
            result = result ^ i
            
        return result
        
    """
    Dict
    
    def singleNumber(self, nums):
        d = {}
        for i in nums:
            if d.has_key(i):
                del d[i]
            else:
                d[i] = 1
        
        d_list = d.items()        
        return d_list[0][0]
    """
