class Solution:
    limit = 1001
    primes = [True] * limit
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for multiple in range(p * p, limit, p):
                primes[multiple] = False
        p += 1
    
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int((str(n)[::-1]))
        mn = min(r, n)
        mx = max(r, n)
        sm = 0
        for i in range(mn, mx + 1):
            if self.primes[i]:
                sm += i
        return sm