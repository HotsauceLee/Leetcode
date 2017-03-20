"""
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

 Notice

min operation will never be called if there is no number in the stack.

Have you met this question in a real interview? Yes
Example
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1
"""

# ============= double stack ============
# Time: O(1) for all operations
# Space: O(2n). n - # of elements in the stack
# Trap: push min again if the new number if bigger than smallest
class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_stack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if self.min_stack:
            smallest = self.min_stack[-1]
            if number < smallest:
                self.min_stack.append(number)
            else:
                self.min_stack.append(smallest)
        else:
            self.min_stack.append(number)

    def pop(self):
        # pop and return the top item in stack
        popped = self.stack.pop()
        self.min_stack.pop()
        return popped

    def min(self):
        # return the minimum number in stack
        return self.min_stack[-1]
