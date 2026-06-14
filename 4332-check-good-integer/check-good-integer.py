class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        sq = ds = 0
        while n > 0:
            m = n % 10
            sq += m * m
            ds += m
            n //= 10
        return (sq - ds) >= 50