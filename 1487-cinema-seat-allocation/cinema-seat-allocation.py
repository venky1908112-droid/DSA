class Solution:
    def maxNumberOfFamilies(self, rw: int, a: List[List[int]]) -> int:
        a.sort()
        rows = 0
        ans = 0
        n = len(a)
        i = 0
        while i < n:
            rows += 1
            x, y = a[i]
            r = 0
            while i < n and x == a[i][0]:
                r = r | (1 << (10 - a[i][1]))
                i += 1
            r >>= 1
            end = 9
            while end >= 4:
                if r & 15 == 0:
                    ans += 1
                    r >>= 4
                    end -= 4
                else:
                    r >>= 2
                    end -= 2
        return ans + (rw - rows) * 2 