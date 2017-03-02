# =========== Stack ============
# Time: O(n)
# Space: O(n)
class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        # Write your code here
        if not s:
            return ""

        stack = []
        number = 0
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == '[':
                stack.append(str(number))
                number = 0
            elif c == ']':
                sub_str = self.pop_stack(stack)
                repeat = int(stack.pop())
                for i in xrange(repeat):
                    stack.append(sub_str)
            else:
                stack.append(c)
                
        return self.pop_stack(stack)
        
    def pop_stack(self, stack):
        q = collections.deque()
        while stack and not stack[-1].isdigit():
            q.appendleft(stack.pop())
            
        return ''.join(q)
