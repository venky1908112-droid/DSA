class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        res = []
        for x, y in intervals[1:]:
            if y <= curr_end:
                continue
            elif curr_end < x:
                res.append([curr_start, curr_end])
                curr_start = x
                curr_end = y
            else:
                curr_end = max(curr_end, y)
        if not res or res[-1] != [curr_start, curr_end]:
            res.append([curr_start, curr_end])
        return res