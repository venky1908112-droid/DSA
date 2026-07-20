class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[((i * n + j + k) % (m * n)) // n][(j + k) % n] = grid[i][j]
        return res