class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs(30 * hour - 5.5 * minutes)
        return min(ans, 360 - ans)