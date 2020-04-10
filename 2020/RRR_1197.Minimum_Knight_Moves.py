"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #return self.bfs(x, y)
        return self.dp(x, y)

    def bfs(self, x, y):
        q = collections.deque([(0, 0)])
        visited = set((0, 0))
        delta_x = [-2, -1, 1, 2, 2, 1, -1, -2]
        delta_y = [1, 2, 2, 1, -1, -2, -2, -1]
        steps = 0
        while q:
            cur_level = len(q)
            for _ in range(cur_level):
                cur_x, cur_y = q.popleft()
                if cur_x == x and cur_y == y:
                    return steps
                for i in range(len(delta_x)):
                    next_cell = (cur_x + delta_x[i], cur_y + delta_y[i])
                    if next_cell not in visited:
                        visited.add(next_cell)
                        q.append(next_cell)
            steps += 1

    @functools.lru_cache # memorization, same as passing along a dict    
    def dp(self, x, y):
        """
        Don't have to worry about direction at all, the
        steps it take to go to the center are the same
        from all 4 corners.
        
        In each step we only care about the minimum step
        of previous steps + 1, and the previous steps are
        from x + y <= 3.
        
        But when hits (1, 0), (0, 1), (1, 1), (2, 0),
        (0, 2), it could miss (0, 0), so we just return
        the minimum steps from those cells.
        
        Also needs memorization because after missing (0, 0) 
        it will circle back because of x, y = abs(x), abs(y)
        which will cause infinite loop.
        """
        x, y = abs(x), abs(y)
        if x + y == 0:
            return 0
        if x + y == 2:
            return 2
        if x + y == 1:
            return 3
        return min(self.dp(x-1, y-2), self.dp(x-2, y-1)) + 1
