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
                    char_save = board[r][c]
                    board[r][c] = '#'
                    if self.__dfs(board, r, c, 1, word):
                        return True
                    board[r][c] = char_save
                    
        return False
        
    def __dfs(self, board, cur_row, cur_col, cur_char, word):
        if cur_char == len(word):
            return True
            
        for i in xrange(4):
            next_row = cur_row + self.delta_row[i]
            next_col = cur_col + self.delta_col[i]
            if (self.__inbound(next_row, next_col) and board[next_row][next_col] == word[cur_char]):
                char_save = board[next_row][next_col]
                board[next_row][next_col] = '#'
                if self.__dfs(board, next_row, next_col, cur_char + 1, word):
                    return True
                board[next_row][next_col] = char_save

    def __inbound(self, row, col):
        return 0 <= row < self.len_row and 0 <= col < self.len_col
            
        
            
        
