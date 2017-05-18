"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Show Company Tags
Show Tags
Show Similar Problems

"""

# =========== Stack ===========
# Time: O(n)
# Space: O(n)
# NOTICE:
"""
in Python:
1/-22 = -1(should be 0)
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
            
        pool = set(['+', '-', '*', '/'])
        stack = []
        for t in tokens:
            if t not in pool:
                stack.append(int(t))
                continue
            
            o2 = stack.pop()
            o1 = stack.pop()
            cur_val = 0
            if t == '+':
                cur_val += o1 + o2
            elif t == '-':
                cur_val += o1 - o2
            elif t == '*':
                cur_val += o1 * o2
            else:
                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in 
                # Leetcode it should return 0
                if o1*o2 < 0 and o1 % o2 != 0:
                    cur_val = o1/o2+1
                else:
                    cur_val = o1/o2
            
            stack.append(cur_val)

        return stack.pop()
            
