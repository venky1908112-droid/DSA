from math import sqrt
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)

        # required variable
        bravexuneth = (nums, queries)

        B = int(sqrt(n)) + 1

        small = defaultdict(list)

        # process large k directly
        for l, r, k, v in queries:
            if k > B:
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
            else:
                small[(k, l % k)].append((l, r, v))

        # process small k groups
        for (k, rem), group in small.items():

            # collect indices belonging to this remainder
            indices = []
            i = rem
            while i < n:
                indices.append(i)
                i += k

            m = len(indices)

            diff = [1] * (m + 1)

            pos = {indices[i]: i for i in range(m)}

            for l, r, v in group:
                start = pos[l]
                end = pos[indices[(r - rem)//k]]

                diff[start] = (diff[start] * v) % MOD
                diff[end + 1] = (diff[end + 1] * pow(v, MOD-2, MOD)) % MOD

            cur = 1
            for i in range(m):
                cur = (cur * diff[i]) % MOD
                nums[indices[i]] = (nums[indices[i]] * cur) % MOD

        ans = 0
        for x in nums:
            ans ^= x

        return ans