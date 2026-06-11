from collections import deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for i in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        """1 : [2, 3]
        2 : [1]
        3 : [4, 5]
        4 : [3]
        5 : [3]
"""
        q = deque()
        q.append((1, 0))
        mx_depth = 0
        visited = [False] * (n + 1)
        while q:
            node, depth = q.popleft()
            visited[node] = True
            mx_depth = max(mx_depth, depth)
            for child in adj[node]:
                if not visited[child]:
                    q.append((child, depth + 1))
                    visited[child] = True
        return pow(2, mx_depth - 1, 10 ** 9 + 7)