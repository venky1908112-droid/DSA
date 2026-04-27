class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = {
                    1: [(0, -1), (0, 1)],
                    2: [(-1, 0), (1, 0)],
                    3: [(0, -1), (1, 0)],
                    4: [(0, 1), (1, 0)],
                    5: [(0, -1), (-1, 0)],
                    6: [(-1, 0), (0, 1)]
                }
    def dfs(self, grid, i, j, visited):
        if i == self.m -1 and j == self.n-1:
            return True
        visited[i][j] = True
        for dx, dy in self.directions[grid[i][j]]:
            new_x, new_y = i + dx, j + dy

            if new_x < 0 or new_x >= self.m or new_y < 0 or new_y >= self.n or visited[new_x][new_y]:
                continue

            for bx, by in self.directions[grid[new_x][new_y]]:
                if new_x + bx == i and new_y + by == j:
                    if self.dfs( grid, new_x, new_y, visited):
                        return True
        return False


    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.m = len(grid)
        self.n = len(grid[0])
        visited = [[False] * self.n for _ in range(self.m)]
        return self.dfs(grid, 0, 0, visited)