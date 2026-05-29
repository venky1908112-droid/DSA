class Solution:
    def minElement(self, nums: List[int]) -> int:
        mn = float('inf')
        for num in nums:
            s = 0
            for digit in str(num):
                s += int(digit)
            mn = min(mn, s)
        return mn