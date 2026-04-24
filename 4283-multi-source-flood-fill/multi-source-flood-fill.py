from collections import deque
class Solution:
    def colorGrid(self, m: int, n: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key = lambda x : x[2], reverse = True)
        dq = deque()
        matrix = [[0] * n for _ in range(m)]
        for r, c, color in sources:
            matrix[r][c] = color
            dq.append((r, c, color))
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]
        while dq:
            r, c, color = dq.popleft()
            for i in range(4):
                newr, newc = r + row[i], c + col[i]
                if 0 <= newr < m and 0 <= newc < n and matrix[newr][newc] == 0:
                    matrix[newr][newc] = color
                    dq.append((newr, newc, color))
        return matrix