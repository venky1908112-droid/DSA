from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = set()
        q = deque()
        q.append(start)
        seen.add(start)
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            p1 = i - arr[i]
            p2 = i + arr[i]
            if 0 <= p1 and p1 not in seen:
                q.append(p1)
                seen.add(p1)
            if p2 < n and p2 not in seen:
                q.append(p2)
                seen.add(p2)
        return False
