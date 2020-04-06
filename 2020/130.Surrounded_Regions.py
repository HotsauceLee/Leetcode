"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        self.b = board
        self.rows = len(self.b)
        self.cols = len(self.b[0])
        
        # get border cells
        from itertools import product
        borders = list(product([0, self.rows - 1], range(self.cols))) + \
                  list(product(range(self.rows), [0, self.cols - 1]))
        
        # mark Os on border cells E, so that later we can
        # just traverse th whole board and mark the remaining
        # Os as X because we know they are the trapped ones
        for row, col in borders:
            #self.dfs(row, col)
            self.bfs(row, col)
            
        # mark Os X and Es O
        for r in range(self.rows):
            for c in range(self.cols):
                if self.b[r][c] == 'O': self.b[r][c] = 'X'
                if self.b[r][c] == 'E': self.b[r][c] = 'O'
                    
    def dfs(self, row, col):
        """
        Dive into a neighbor cells first, therefore dfs
        """
        if self.b[row][col] != 'O':
            return
        
        self.b[row][col] = 'E'
        if row - 1 > 0: self.dfs(row - 1, col)
        if row + 1 < self.rows: self.dfs(row + 1, col)
        if col - 1 > 0: self.dfs(row, col - 1)
        if col + 1 < self.cols: self.dfs(row, col + 1)
            
    def bfs(self, row, col):
        """
        Check all neighbor cells first, therefore bfs
        """
        if self.b[row][col] != 'O':
            return
        
        from collections import deque
        q = deque()
        q.append((row, col))
        while q:
            cur_r, cur_c = q.popleft()
            if self.b[cur_r][cur_c] != 'O':
                continue
            self.b[cur_r][cur_c] = 'E'
            if cur_r - 1 > 0: q.append((cur_r - 1, cur_c))
            if cur_r + 1 < self.rows: q.append((cur_r + 1, cur_c))
            if cur_c - 1 > 0: q.append((cur_r, cur_c - 1))
            if cur_c + 1 < self.cols: q.append((cur_r, cur_c + 1))
