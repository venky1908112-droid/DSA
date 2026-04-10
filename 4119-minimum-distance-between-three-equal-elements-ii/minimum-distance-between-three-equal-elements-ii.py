from collections import deque, defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indxs = defaultdict(lambda :deque(maxlen = 3))
        mn = float('inf')
        for i,v in enumerate(nums):
            indxs[v].append(i)
            if len(indxs[v]) == 3:
                f,_, t = indxs[v]
                mn = min(mn, (t - f) * 2)
        return -1 if float('inf') == mn else mn