# ============= Stack =============
# Time: O(N = all nodes)
# Space: O(N = all nodes)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        if not nestedList:
            return 0
            
        q = collections.deque(nestedList)
        result = 0
        level = 0
        while len(q) > 0:
            level += 1
            cur_len = len(q)
            for i in xrange(cur_len):
                cur_node = q.pop()
                if cur_node.isInteger():
                    result += cur_node.getInteger() * level
                else:
                    for next_node in cur_node.getList():
                        q.appendleft(next_node)
                    
        return result
