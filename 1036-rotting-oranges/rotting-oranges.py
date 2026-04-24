from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = grid
        dq = deque()
        one_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i,j,0))
                if grid[i][j] == 1:
                    one_count += 1
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]
        max_time = 0
        while dq:
            i, j, t = dq.popleft()
            max_time = t
            for x in range(4):
                newi = i + row[x]
                newj = j + col[x]
                if 0 <= newi < m and 0 <= newj < n and visited[newi][newj] != 2 and grid[newi][newj] == 1:
                    dq.append((newi, newj, t + 1))
                    visited[newi][newj] = 2
                    one_count -= 1
        if one_count > 0:
            return -1
        return max_time
            
            