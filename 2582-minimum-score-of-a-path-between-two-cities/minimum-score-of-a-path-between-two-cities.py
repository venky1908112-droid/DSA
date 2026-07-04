from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        ans = float('inf')
        seen = set()
        def dfs(node):
            nonlocal ans
            seen.add(node)
            for nei , d in graph[node]:
                ans = min(ans, d)
                if nei not in seen:
                    dfs(nei)
        dfs(1)
        return ans