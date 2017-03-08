# ============ BFS ==============
# Time: O(N = all nodes)
# Space: O(N = all nodes)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
            
        result = 0
        level = 0
        q = collections.deque(nestedList)
        while len(q) > 0:
            cur_len = len(q)
            level += 1
            for i in xrange(cur_len):
                cur_node = q.pop()
                if cur_node.isInteger():
                    result += cur_node.getInteger()*level
                else:
                    for node in cur_node.getList():
                        q.appendleft(node)
                        
        return result
        
