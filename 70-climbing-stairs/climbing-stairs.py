class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        past = 3
        curr = 5
        for _ in range(n - 4):
            temp = curr
            curr += past
            past = temp
        return curr