# ============ DP ===============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        d = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        }
        num_house = len(costs)
        for i in xrange(1, num_house):
            for j in xrange(3):
                costs[i][j] += min(costs[i - 1][d[j][0]], costs[i - 1][d[j][1]])
                
        return min(costs[-1][0], min(costs[-1][1], costs[-1][2]))
