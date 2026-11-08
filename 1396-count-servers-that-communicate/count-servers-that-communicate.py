class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        rows = defaultdict(int)
        columns = defaultdict(int)
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    columns[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if rows[i] > 1 or columns[j] > 1:
                        ans += 1
        return ans