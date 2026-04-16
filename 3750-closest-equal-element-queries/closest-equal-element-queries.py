from collections import defaultdict
from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)

        res = [-1] * len(queries)
        N = len(nums)

        for i, query in enumerate(queries):
            lst = d[nums[query]]
            n = len(lst)

            if n > 1:
                mid = bisect_left(lst, query)

                prev_idx = lst[(mid - 1 + n) % n]
                next_idx = lst[(mid + 1) % n]

                dist1 = abs(query - prev_idx)
                dist2 = abs(query - next_idx)

                dist1 = min(dist1, N - dist1)
                dist2 = min(dist2, N - dist2)

                res[i] = min(dist1, dist2)

        return res