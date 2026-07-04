from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        ans = float('inf')
        visited = set()
        def dfs(node):
            nonlocal ans
            visited.add(node)
            for n, d in graph[node]:
                ans = min(ans, d)
                if n not in visited:
                    dfs(n)
        dfs(1)
        return ans