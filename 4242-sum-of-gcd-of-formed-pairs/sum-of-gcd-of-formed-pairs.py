class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = float('-inf')
        prefix = []
        for x in nums:
            mx = max(mx, x)
            prefix.append(math.gcd(x, mx))
        prefix.sort()
        left = 0
        right = len(prefix) - 1
        res = 0
        while left < right:
            res += math.gcd(prefix[left], prefix[right])
            left += 1
            right -= 1
        return res