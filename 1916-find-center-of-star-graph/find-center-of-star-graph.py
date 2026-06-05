from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        for u, v in edges:
            freq[u] += 1
            freq[v] += 1
        max_val = 0
        ans = 0
        for key, val in freq.items():
            if val > max_val:
                max_val = val
                ans = key
        return ans
            