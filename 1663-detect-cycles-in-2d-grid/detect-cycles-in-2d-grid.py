class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        def dfs(x, y, px, py):
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                if grid[nx][ny] != grid[x][y]:
                    continue

                if nx == px and ny == py:
                    continue
                
                if visited[nx][ny]:
                    return True
                
                if dfs(nx, ny, x, y):
                    return True
            
            return False

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if dfs(i, j, -1, -1):
                    return True
        return False
            