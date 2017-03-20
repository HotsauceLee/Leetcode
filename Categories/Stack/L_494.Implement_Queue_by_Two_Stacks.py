"""
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Have you met this question in a real interview? Yes
Example
push(1)
pop()     // return 1
push(2)
push(3)
top()     // return 2
pop()     // return 2
"""

# Time: push: O(n), pop: O(n), top: O(1)
# Space: O(2n)
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        if self.stack1:
            return self.stack1[0]
        return self.stack2[-1] if self.stack2 else None

    def pop(self):
        # write your code here
        # pop and return the top element
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop() if self.stack2 else None
