from collections import deque, defaultdict
from typing import List

LIMIT = 10**6 + 1

primes = [True] * LIMIT
primes[0] = primes[1] = False

p = 2

while p * p < LIMIT:

    if primes[p]:

        for multiple in range(p * p, LIMIT, p):
            primes[multiple] = False

    p += 1


class Solution:

    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 0

        mx_val = max(nums)

        mp = defaultdict(list)

        for i, val in enumerate(nums):
            mp[val].append(i)

        vis = [False] * n
        vis[0] = True

        q = deque([(0, 0)])

        seen = set()

        while q:

            i, s = q.popleft()

            if i == n - 1:
                return s

            # left jump
            if i - 1 >= 0 and not vis[i - 1]:

                vis[i - 1] = True
                q.append((i - 1, s + 1))

            # right jump
            if i + 1 < n and not vis[i + 1]:

                vis[i + 1] = True
                q.append((i + 1, s + 1))

            # teleportation
            if not primes[nums[i]] or nums[i] in seen:
                continue

            for multiple in range(nums[i], mx_val + 1, nums[i]):

                for nxt in mp[multiple]:

                    if not vis[nxt]:

                        vis[nxt] = True
                        q.append((nxt, s + 1))

            seen.add(nums[i])

        return -1