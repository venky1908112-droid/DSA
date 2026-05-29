class Solution:
    def minElement(self, nums: List[int]) -> int:
        mn = float('inf')
        for num in nums:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            mn = min(mn, s)
        return mn