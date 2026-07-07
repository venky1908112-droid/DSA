class Solution:
    def sumAndMultiply(self, n: int) -> int:
        r = 0
        sm = 0
        for x in str(n):
            v = int(x)
            if v != 0:
                sm += v
                r = r * 10 + v
        return sm * r 