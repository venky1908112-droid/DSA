from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        islands = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or visited[i][j]:
                    continue
                islands += 1
                q.append((i, j))
                visited[i][j] = True
                while q:
                    for _ in range(len(q)):
                        x, y = q.popleft()
                        for dx , dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '1':
                                q.append((nx, ny))
                                visited[nx][ny] = True
        return islands
            