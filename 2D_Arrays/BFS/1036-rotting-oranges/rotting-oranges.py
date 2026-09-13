class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        
        n = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        one_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    one_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        time = 0
        if one_count == 0:
            return 0
        while q and one_count > 0:
            time += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        one_count -= 1
                        q.append((nx, ny))
        return time if one_count == 0 else -1
