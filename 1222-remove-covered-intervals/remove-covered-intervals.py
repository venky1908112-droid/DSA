class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        removed = [False] * n
        for i in range(n):
            if removed[i]:
                continue
            for j in range(i + 1,n):
                if intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1]:
                    removed[j] = True
                elif intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                    removed[i] = True
                    break
        return n - sum(removed)