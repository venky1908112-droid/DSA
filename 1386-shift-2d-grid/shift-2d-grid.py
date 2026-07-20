class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        a = []
        for row in grid:
            a.extend(row)
        a = a[-k : ] + a[ : -k]
        x = 0
        res = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(a[x])
                x += 1
            res.append(temp)
        return res
