from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = set()
        q = deque()
        q.append((start, arr[start]))
        seen.add(start)
        while q:
            idx, val = q.popleft()
            if val == 0:
                return True
            p1 = idx - val
            p2 = idx + val
            if p1 >= 0 and p1 not in seen:
                q.append((p1, arr[p1]))
                seen.add(p1)
            if p2 < n and p2 not in seen:
                q.append((p2, arr[p2]))
                seen.add(p2)
        return False