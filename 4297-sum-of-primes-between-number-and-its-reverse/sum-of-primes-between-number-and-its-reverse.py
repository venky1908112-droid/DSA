class Solution:
    is_primes = [True] * 1001
    p = 2
    is_primes[0] = is_primes[1] = False
    while p * p <= 1000:
        if is_primes[p]:
            for multiple in range(p * p, 1001, p):
                is_primes[multiple] = False
        p += 1
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = int(str(n)[::-1])
        mn = min(rev, n)
        mx = max(rev, n)
        s = 0
        for i in range(mn, mx + 1):
            if self.is_primes[i]:
                s += i
        return s