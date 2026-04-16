from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(list)
        n = len(nums)
        
        # Step 1: store indices of each value
        for i, x in enumerate(nums):
            d[x].append(i)
        
        # Step 2: precompute answers for every index
        ans = [-1] * n
        
        for val in d:
            lst = d[val]
            k = len(lst)
            
            if k == 1:
                continue
            
            for i in range(k):
                cur = lst[i]
                
                prev = lst[i - 1] if i > 0 else lst[-1]
                next_ = lst[i + 1] if i < k - 1 else lst[0]
                
                d1 = abs(cur - prev)
                d2 = abs(next_ - cur)
                
                ans[cur] = min(d1, n - d1, d2, n - d2)
        
        # Step 3: answer queries in O(1)
        return [ans[q] for q in queries]