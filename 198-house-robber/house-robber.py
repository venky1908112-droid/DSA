class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            if n == 1:
                return nums[0]
            return max(nums[0] , nums[1])
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        dp[n - 2] = nums[n - 2]
        dp[n - 3] = nums[n - 1] + nums[n - 3]
        for i in range(n - 4, -1, -1):
            dp[i] = max(dp[i + 2], dp[i + 3]) + nums[i]
        return max(dp[0], dp[1])