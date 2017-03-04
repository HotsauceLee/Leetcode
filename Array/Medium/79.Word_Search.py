# ============== DFS ==================
# Time:
# Space:
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if len(word) == 0:
            return True
        self.len_row, self.len_col = len(board), len(board[0])
        self.delta_row = [1, -1, 0, 0]
        self.delta_col = [0, 0, 1, -1]
        if self.len_row*self.len_col < len(word):
            return False
            
        for r in xrange(self.len_row):
            for c in xrange(self.len_col):
                if board[r][c] == word[0]:
                    if len(word) == 1:
                        return True
                    visited = [[False]*self.len_col for i in xrange(self.len_row)]
                    visited[r][c] = True
                    if self.__dfs(visited, board, r, c, 1, word):
                        return True
                    
        return False
        
    def __dfs(self, visited, board, cur_row, cur_col, cur_char, word):
        if cur_char == len(word):
            return True
            
        for i in xrange(4):
            next_row = cur_row + self.delta_row[i]
            next_col = cur_col + self.delta_col[i]
            if (self.__inbound(next_row, next_col, len(board) - 1, len(board[0]) - 1)
                    and not visited[next_row][next_col]
                    and board[next_row][next_col] == word[cur_char]):
                visited[next_row][next_col] = True
                if self.__dfs(visited, board, next_row, next_col, cur_char + 1, word):
                    return True
                visited[next_row][next_col] = False
    
    # Won't work
    def __bfs(self, board, row, col, word):
        
        visited = [[False]*len(board[0]) for i in xrange(len(board))]
        visited[row][col] = True
        next_char = 1
        q = collections.deque([(row, col)])
        while len(q):
            cur_level = len(q)
            for i in xrange(cur_level):
                cur_row, cur_col = q.pop()
                for i in xrange(4):
                    next_row = cur_row + self.delta_row[i]
                    next_col = cur_col + self.delta_col[i]
                    if (self.__inbound(next_row, next_col, len(board) - 1, len(board[0]) - 1)
                            and not visited[next_row][next_col]
                            and board[next_row][next_col] == word[next_char]):
                        if next_char == len(word) - 1:
                            return True
                        q.appendleft((next_row, next_col))
                        visited[next_row][next_col] = True
            next_char += 1
            if next_char >= len(word):
                break
                    
        return False
            
    def __inbound(self, row, col, max_row, max_col):
        return 0 <= row <= max_row and 0 <= col <= max_col
            
        
