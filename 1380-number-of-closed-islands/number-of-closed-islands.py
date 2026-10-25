from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(n):
            if grid[0][i] == 0:
                q.append((0, i))
            if grid[m - 1][i] == 0:
                q.append((m -1, i))
        for i in range(1,m - 1):
            if grid[i][0] == 0:
                q.append((i, 0))
            if grid[i][n - 1] == 0:
                q.append((i, n - 1))
        def bfs():
            while q:
                x, y = q.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1 and not visited[nx][ny]:
                        q.append((nx, ny))
        bfs()
        islands = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if visited[i][j] or grid[i][j]:
                    continue
                islands += 1
                q.append((i, j))
                bfs()
        return islands
