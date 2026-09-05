class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        past = 0
        curr = 1
        for _ in range(n - 1):
            temp = curr
            curr = past + curr
            past = temp
        return curr