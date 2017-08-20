# =========== Old way ============
# Time: add: O(1), find: O(n)
# Space: O(n)
# NOTICE: think about trade-off
"""
The big data test only have the condition that lots of add and few find. In fact, there has to be one operation's time complexity is O(n) and the other is O(1), no matter add or find. So clearly there's trade off when solve this problem, prefer quick find or quick add.

If consider more find and less add or we only care time complexity in finding.For example, add operation can be pre-done.
"""
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.store.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        d = set()
        for n in self.store:
            if (value - n) in d:
                return True
            d.add(n)
                
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
