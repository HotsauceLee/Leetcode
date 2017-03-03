# ============== Binary Search =================
# Time: O(nlog(n))
# Space: O(1)
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or k == 0: return 0
        begin, end = 1, max(L)
        while begin + 1 < end:
            mid = (begin + end)/2
            
            cur_result = 0
            for l in L:
                cur_result += l/mid
                
            if cur_result >= k:
                begin = mid
            else:
                end = mid
        
        begin_result, end_result = 0, 0
        for l in L:
            begin_result += l/begin
            end_result += l/end
            
        if end_result >= k:
            return end
        if begin_result >= k:
            return begin
            
        return 0
            
            
