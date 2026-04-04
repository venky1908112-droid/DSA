class Solution:
    def decodeCiphertext(self, s: str, m: int) -> str:
        if m <= 1:
            return s
        n = len(s) // m
        res = []
        for i in range(n):
            r = 0
            c = i
            while r < m and c < n:
                res.append(s[r * n + c])
                r += 1
                c += 1
        return "".join(res).rstrip()