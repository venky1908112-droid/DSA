class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        
        for i in range(1, m):
            grid[i][n-1] = '.'
        for i in range(n):
            grid[0][i] = '.'
        new = []
        for row in grid:
            new.append(''.join(row))
        return new