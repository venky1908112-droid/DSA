class Solution:
    def maxNumberOfFamilies(self, total_rows: int, a: List[List[int]]) -> int:
        a.sort()
        present_rows = 0
        ans = 0
        n = len(a)
        i = 0
        while i < n:
            present_rows += 1
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
                    continue
                
                r >>= 2
                end -= 2
                
        return ans + (total_rows - present_rows) * 2 