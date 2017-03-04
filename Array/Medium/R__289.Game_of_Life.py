# ============ Use different number to store prev and cur state
# Time: O(2mn)
# Space: O(1)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        delta_x = [1, 1, 1, -1, -1, -1, 0, 0]
        delta_y = [-1, 0, 1, -1, 0, 1, -1, 1]
        len_x, len_y = len(board), len(board[0])
        
        def inbound(x, y):
            return 0 <= x < len_x and 0 <= y < len_y

        for x in xrange(len_x):
            for y in xrange(len_y):
                live_count = 0
                for i in xrange(8):
                    neighbor_x = x + delta_x[i]
                    neighbor_y = y + delta_y[i]
                    if inbound(neighbor_x, neighbor_y):
                        neighbor_val = board[neighbor_x][neighbor_y]
                        # 2 means was dead then back to life, 3 means was live then dead
                        if neighbor_val == 1 or neighbor_val == 3:
                            live_count += 1
                if board[x][y] and (live_count < 2 or live_count > 3):
                    board[x][y] = 3
                elif not board[x][y] and live_count == 3:
                    board[x][y] = 2
                    
        for x in xrange(len_x):
            for y in xrange(len_y):
                if board[x][y] == 2:
                    board[x][y] = 1
                if board[x][y] == 3:
                    board[x][y] = 0
                    
                    
# ======== Follow up ============
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""
Solution:

"""
