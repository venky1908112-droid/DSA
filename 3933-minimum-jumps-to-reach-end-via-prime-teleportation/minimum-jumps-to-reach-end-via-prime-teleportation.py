from collections import deque, defaultdict
class Solution:
    limit = 10 ** 6 + 1

    primes = [True] * limit 
    primes[0] = primes[1] = False
    p = 2
    while p * p < limit:
        if primes[p]:
            for multiple in range(p * p, limit, p):
                primes[multiple] = False
        p += 1
    
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        visited = [False] * n
        max_val = -1
        mp = defaultdict(list)
        for i, x in enumerate(nums):
            mp[x].append(i)
            max_val = max(max_val, x)
        q = deque([(0, 0)]) # (idx, steps)
        visited[0] = True
        seen = set()
        while q:
            i, s = q.popleft()

            if i == n - 1:
                return s

            if i - 1 >= 0 and not visited[i - 1]:
                q.append((i - 1, s + 1))
                visited[i - 1] = True
            
            if i + 1 < n and not visited[i + 1]:
                q.append((i + 1, s + 1))
                visited[i + 1] = True
            
            if not self.primes[nums[i]] or nums[i] in seen:
                continue
            
            for multiple in range(nums[i], max_val + 1, nums[i]):
                if multiple not in mp:
                    continue
                for idx in mp[multiple]:
                    if not visited[idx]:
                        visited[idx] = True
                        q.append((idx, s + 1))
            seen.add(nums[i])