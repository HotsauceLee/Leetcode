"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class UnionFind:
    def __init__(self, nodes):
        self.fathers = {}
        self.unique_sets = len(nodes)
        for n in nodes:
            self.add(n)

    def add(self, node):
        """
        Add nodes on the go, no need to add all of
        them at initialzation.
        """
        if node not in self.fathers:
            self.fathers[node] = node
            self.unique_sets += 1

    def find(self, node):
        if self.fathers[node] == node:
            return node

        f = self.find(self.fathers[node])
        self.fathers[node] = f
        return f

    def union(self, node1, node2):
        f1 = self.find(node1)
        f2 = self.find(node2)
        if f1 != f2:
            self.fathers[f1] = f2
            self.unique_sets -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        #return self.union_find(grid)
        return self.bfs(grid)

    def inbound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def union_find(self, grid):
        """
        T: O(M*N) https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Find
        S: O(M*N) uf object keeps all nodes
        """
        # O(N)
        uf = UnionFind([])

        delta_row = [-1, 1, 0, 0]
        delta_col = [0, 0, -1, 1]
        # O(4N)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != '1':
                    continue
                uf.add((row, col))
                grid[row][col] = '0'
                for delta in range(len(delta_row)):
                    cur_row = row + delta_row[delta]
                    cur_col = col + delta_col[delta]
                    if self.inbound(cur_row, cur_col, grid) and grid[cur_row][cur_col] == '1':
                        uf.add((cur_row, cur_col))
                        uf.union((row, col), (cur_row, cur_col))

        return uf.unique_sets

    def bfs(self, grid):
        """
        NOTE: Marking a cell '0' before putting it into the queue
        could prevent it's neighbors putting the same of their
        neightbors into the queue

        T: O(M*N)
        S: O(min(M, N))
        Explanation of BFS Space Complexity: Min(M, N).
        Think about an example where dif(M, N) is big like 3x1000 grid. And the worst case is when we start from the middle of the grid.
        Imagine how the processed points form a shape in the grid. It will be like a diamond and at some point, it will reach the longer edge of the grid. The possible shape at time t would be:
        ......QXXXQ.........
        ....QXXXXXQ........
        ......QXXXQ.........
        So in this specific example (Q: points in the queue, .: not processed, X: processed) the number of the items in the queue is proportional with 3 because the smallest side limits the expanding.
        So the actual value will be Min(M, N)*a+b but since a and b are constants and independent than M and N, Space complexity becomes Min(M, N).
        """
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.__bfs_helper(row, col, grid)
                    result += 1
        return result

    def __bfs_helper(self, row, col, grid):
        q = collections.deque([(row, col)])
        grid[row][col] = '0' # prevents duplication
        while q:
            node = q.popleft()
            cur_row, cur_col = node
            if cur_row - 1 >= 0 and grid[cur_row-1][cur_col] == '1':
                q.append((cur_row-1, cur_col))
                grid[cur_row-1][cur_col] = '0'
            if cur_row + 1 < len(grid) and grid[cur_row+1][cur_col] == '1':
                q.append((cur_row+1, cur_col))
                grid[cur_row+1][cur_col] = '0'
            if cur_col - 1 >= 0 and grid[cur_row][cur_col-1] == '1':
                q.append((cur_row, cur_col-1))
                grid[cur_row][cur_col-1] = '0'
            if cur_col + 1 < len(grid[0]) and grid[cur_row][cur_col+1] == '1':
                q.append((cur_row, cur_col+1))
                grid[cur_row][cur_col+1] = '0'
