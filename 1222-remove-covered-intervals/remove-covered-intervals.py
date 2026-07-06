class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        ans = 0
        pe = 0
        for a, b in intervals:
            ans += pe < b
            pe = max(b, pe)
        return ans