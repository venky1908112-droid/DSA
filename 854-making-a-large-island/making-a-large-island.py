from collections import deque, defaultdict
class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        group_area = defaultdict(int)
        q = deque()
        #step 1 
        group = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
                q.append((i, j))
                area = 0
                while q:
                    area += 1
                    print(area)
                    x, y = q.popleft()
                    visited[x][y] = True
                    matrix[x][y] = group
                    for dx, dy in directions:
                        nx, ny = dx + x, dy + y
                        if 0 <= nx < m and 0 <= ny < n and (not visited[nx][ny]) and grid[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                group_area[group] = area
                max_area = max(max_area, area)
                group += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        while q:
            union = set()
            x, y = q.popleft()
            area = 0
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    union.add(matrix[nx][ny])
            for val in union:
                area += group_area[val]
            max_area = max(max_area, area + 1)
        return max_area