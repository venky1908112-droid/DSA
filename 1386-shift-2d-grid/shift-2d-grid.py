class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                curr_idx = (i * n + j)
                new_idx = (curr_idx + k) % (m * n)
                r = new_idx // n
                c = new_idx % n
                res[r][c] = grid[i][j]
        return res