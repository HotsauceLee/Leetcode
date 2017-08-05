"""
给你一个 array of int , 让你输出的是 同样size 的 array of int。 
对于每个 position, 输出是右边第一个比他大的数字 。 
for example: you are givien [10,9,11,2,1] , 输出应该是 [11,11,-1,-1,-1]
"""

# ================ stack ===================
# Time: O(n) - each element will be pushed/popped at most once
# Space: O(n)
# Idea: all elements on the right of current position that are smaller than cur is useless
#    pop them out and insert new one in.
# https://stackoverflow.com/questions/22233018/in-an-unsorted-array-replace-every-element-by-the-first-larger-element-to-the-r
tc1 = []
tc2 = None
tc3 = [1,2,3,4,5] # [2,3,4,5,-1]
tc4 = [5,4,3,2,1,9] # [9,9,9,9,9,-1]
tc5 = [3,2,1,4,7,5,8,4] # [4,4,4,7,8,8,-1]

def solution(input):
  if not input:
    return []
    
  stack = []
  from collections import deque
  result = deque()
  for i in input[::-1]:
    while stack and stack[-1] <= i:
      stack.pop()
      
    cur_val = stack[-1] if stack else -1
    result.appendleft(cur_val)
    stack.append(i)
    
  return list(result)
  
print solution(tc1)
print solution(tc2)
print solution(tc3)
print solution(tc4)
print solution(tc5)
