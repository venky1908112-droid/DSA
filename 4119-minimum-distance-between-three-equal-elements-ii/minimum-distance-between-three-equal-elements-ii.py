from collections import defaultdict, deque
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indx = defaultdict(deque)
        mn = float('inf')
        for i, val in enumerate(nums):
            indx[val].append(i)
            if len(indx[val]) > 3:
                indx[val].popleft()
            if len(indx[val]) == 3:
                f, _, l = indx[val]
                mn = min(mn, (l - f) * 2)
        return -1 if mn == float('inf') else mn