class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(ls, ld, ws, wd):
            m = float('inf')
            for i in range(len(ls)):
                m = min(m, ls[i] + ld[i])
            ans = float('inf')
            for i in range(len(ws)):
                ans = min(ans, max(m, ws[i]) + wd[i])
            return ans
        return min(solve(landStartTime, landDuration, waterStartTime, waterDuration), solve( waterStartTime, waterDuration, landStartTime, landDuration))