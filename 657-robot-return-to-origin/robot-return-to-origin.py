class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0,0
        for m in moves:
            if m == 'U':
                x += 1
            elif m == 'D':
                x -= 1
            elif m == 'L':
                y -= 1
            else:
                y += 1
        return x == y == 0