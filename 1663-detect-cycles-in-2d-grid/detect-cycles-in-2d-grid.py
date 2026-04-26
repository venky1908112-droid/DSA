from collections import deque
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def bfs(i , j):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            q = deque()
            q.append((i, j, -1, -1))
            visited[i][j] = True
            while q:
                x, y, px, py = q.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if grid[x][y] != grid[nx][ny]:
                        continue
                    if px == nx and py == ny:
                        continue
                    if visited[nx][ny]:
                        return True
                    visited[nx][ny] = True
                    q.append((nx, ny, x, y))
            return False
                    

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(i,j):
                        return True
        return False