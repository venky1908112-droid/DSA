class Solution:
    def maxNumberOfFamilies(self, total_rows: int, a: List[List[int]]) -> int:
        a.sort()
        i = 0
        n = len(a)
        ans = 0
        present_rows = 0
        while i < n:
            present_rows += 1
            x, y = a[i]
            bit = 0
            while i < n and a[i][0] == x:
                bit |= (1 << (10 - a[i][1]))
                i += 1
            bit >>= 1
            end = 9
            while end > 4:
                if bit & 15 == 0:
                    ans += 1
                    bit >>= 4
                    end -= 4
                    continue
                bit >>= 2
                end -= 2
        return ans + (total_rows - present_rows) * 2
