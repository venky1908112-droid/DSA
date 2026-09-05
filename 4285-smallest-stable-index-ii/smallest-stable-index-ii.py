class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        a = [0] * n
        mn = float('inf')
        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            a[i] = mn
        mx = -1
        for i in range(n):
            mx = max(mx, nums[i])
            mn = a[i]
            if mx - mn <= k:
                return i
        return -1
        