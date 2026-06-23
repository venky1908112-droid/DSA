class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        x = len(word)
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        options = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, k):
            if grid[i][j] != word[k]:
                return False
            if k == x - 1:
                return True

            visited[i][j] = True
            for a, b in options:
                ni, nj = i + a, j + b
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if dfs(ni, nj, k + 1):
                        visited[i][j] = False
                        return True
            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False