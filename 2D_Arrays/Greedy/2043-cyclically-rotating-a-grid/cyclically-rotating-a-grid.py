class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            val = []
            top = left = layer
            bottom = m - layer - 1
            right = n - layer - 1
            #top row
            for i in range(left, right + 1):
                val.append(grid[top][i])
            #right side
            for i in range(top + 1, bottom):
                val.append(grid[i][right])
            #down part
            for i in range(right, left - 1, -1):
                val.append(grid[bottom][i])
            #left part
            for i in range(bottom - 1, top, -1):
                val.append(grid[i][left])
            r = k % len(val)
            val = val[r:] + val[:r]
            idx = 0
            for i in range(left, right + 1):
                grid[top][i] = val[idx]
                idx += 1
            #right side
            for i in range(top + 1, bottom):
                grid[i][right] = val[idx]
                idx += 1
            #down part
            for i in range(right, left - 1, -1):
                grid[bottom][i] = val[idx]
                idx += 1 
            #left part
            for i in range(bottom - 1, top, -1):
                grid[i][left] = val[idx]
                idx += 1
        return grid
