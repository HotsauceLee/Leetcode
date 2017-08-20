# ============= Backtracking ==========
# Time: ?
# Space: ?
# NOTICE:
"""
Actually, factors of an integer n (except for 1 and n) 
are always between 1 and sqrt(n), so you do not have to 
check those numbers between sqrt(n) and n. However, in 
your method, we need to check n, so I added a check, 
when i is greater than sqrt(n), i will jump directly 
to n. This little change improved a lot. Thank you!
"""
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []

        def dfs(start, cur_path, remain, result):
            if remain == 1:
                result.append(cur_path[:])
                return
            
            for i in xrange(start, int(math.sqrt(remain)) + 1):
                if remain % i != 0:
                    continue
                
                cur_path.append(i)
                dfs(i, cur_path, remain/i, result)
                cur_path.pop()
                
            cur_path.append(remain)
            dfs(remain, cur_path, 1, result)
            cur_path.pop()
        
        result = []
        dfs(2, [], n, result)
        result.pop()
        return result
                
                
                
                
