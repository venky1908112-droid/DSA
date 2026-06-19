class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        s = 0
        for x in gain:
            s += x
            mx = max(mx, s)
        return mx