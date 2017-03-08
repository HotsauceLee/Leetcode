"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

 Notice

You don't need to implement the remove method.

Have you met this question in a real interview? Yes
Example
Given the list [[1,1],2,[1,1]], By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Given the list [1,[4,[6]]], By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""
# ============ Stack ============
# Time: init: O(N = all ints) next: O(1) hasNext: O(1)
# Space: O(N = all ints)

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

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        while nestedList:
            if nestedList[-1].isInteger():
                self.stack.append(nestedList.pop().getInteger())
            else:
                for node in nestedList.pop().getList():
                    nestedList.append(node)
        
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return len(self.stack) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
