class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        return abs(m.count('L') - m.count('R')) + m.count('_')