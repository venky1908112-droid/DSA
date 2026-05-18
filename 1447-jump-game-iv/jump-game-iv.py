from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        idx_pos = defaultdict(list)
        for i, x in enumerate(arr):
            idx_pos[x].append(i)
        visited = [False] * n
        q = deque()
        q.append((0, 0))
        seen = set()
        while q:
            idx, steps = q.popleft()

            if idx == n - 1:
                return steps
            
            if visited[idx]:
                continue
            #case 1
            if idx - 1 >= 0 and not visited[idx - 1]:
                q.append((idx - 1, steps + 1))
            #case2
            if idx + 1 < n and not visited[idx + 1]:
                q.append((idx + 1, steps + 1))
            #case 3
            if arr[idx] not in seen:
                for i in idx_pos[arr[idx]]:
                    if i != idx and not visited[i]:
                        q.append((i, steps + 1))
            
            visited[idx] = True
            seen.add(arr[idx])
            
            
            

        