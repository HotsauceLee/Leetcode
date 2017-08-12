"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Seen this question in a real interview before?   Yes  
"""

# ============== BFS ==============
# Time: O(m*n)
# Space: O(m*n)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        len_row, len_col = len(board), len(board[0])
        
        def in_range(row, col):
            return 0 <= row < len_row and 0 <= col < len_col
        
        delta_row = [0, 0, 1, -1]
        delta_col = [1, -1, 0, 0]
        
        def bfs(visited, board, row, col):
            q = collections.deque([(row, col)])
            cur_key = row*len_col + col
            visited.add(cur_key)
            while len(q) > 0:
                cur_row, cur_col = q.pop()
                for i in xrange(4):
                    next_row = cur_row + delta_row[i]
                    next_col = cur_col + delta_col[i]
                    next_key = next_row*len_col + next_col
                    if in_range(next_row, next_col) and next_key not in visited and board[next_row][next_col] == 'O':
                        visited.add(next_key)
                        q.appendleft((next_row, next_col))
        
        # find Os on the boundary
        v = set()
        # up to down
        left_col, right_col = 0, len_col - 1
        for row in xrange(len_row):
            left_key = row*len_col
            if left_key not in v and board[row][left_col] == 'O':
                bfs(v, board, row, left_col)
                
            right_key = row*len_col + right_col
            if right_key not in v and board[row][right_col] == 'O':
                bfs(v, board, row, right_col)
        
        # left to right
        up_row, down_row = 0, len_row - 1
        for col in xrange(len_col):
            up_key = col
            if up_key not in v and board[up_row][col] == 'O':
                bfs(v, board, up_row, col)
                
            down_key = down_row*len_col + col
            if down_key not in v and board[down_row][col] == 'O':
                bfs(v, board, down_row, col)
        
        # turn the rest of Os to X
        for row in xrange(1, len_row - 1):
            for col in xrange(1, len_col - 1):
                cur_key = row*len_col + col
                if cur_key not in v and board[row][col] == 'O':
                    board[row][col] = 'X'
            
