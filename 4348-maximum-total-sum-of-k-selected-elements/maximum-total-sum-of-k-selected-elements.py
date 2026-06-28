class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        res = 0
        for i in range(k):
            if mul > 0:
                res += nums[i] * mul
                mul -= 1
            else:
                res += nums[i]
        return res