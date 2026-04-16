from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(list)
        
        # Build index map
        for i, x in enumerate(nums):
            d[x].append(i)
        
        n = len(nums)
        res = [-1] * len(queries)
        
        for i, q in enumerate(queries):
            lst = d[nums[q]]
            
            if len(lst) == 1:
                continue
            
            # Find position of q in lst
            pos = bisect_left(lst, q)
            
            # Previous index (circular)
            prev_idx = lst[pos - 1] if pos > 0 else lst[-1]
            
            # Next index (circular)
            next_idx = lst[pos + 1] if pos < len(lst) - 1 else lst[0]
            
            # Compute circular distances
            d1 = abs(q - prev_idx)
            d2 = abs(next_idx - q)
            
            res[i] = min(d1, n - d1, d2, n - d2)
        
        return res