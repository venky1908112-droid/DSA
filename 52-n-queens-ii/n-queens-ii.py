class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        board = [['.'] * n for _ in range(n)]
        count = 0
        
        def isvalid(x, y):
            for i in range(x):
                if board[i][y] == 'Q':
                    return False
                if (y - (i + 1)) >= 0 and board[x - (i + 1)][y - (i + 1)]  == 'Q':
                    return False
                if (y + (i + 1)) < n and board[x - (i + 1)][y + (i + 1)]  == 'Q': 
                    return False
            return True

        def solve(row, board, n):
            nonlocal count
            if row == n:
                count += 1
                return 
            for i in range(n):
                if isvalid(row, i):
                    board[row][i] = 'Q'
                    solve(row + 1, board, n)
                    board[row][i] = '.'
        
        solve(0, board, n)

        return count