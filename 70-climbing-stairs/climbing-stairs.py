class Solution(object):
    def climbStairs(self, n):
        dp = [-1] * n
        def backtrack(s):
            if s > n:
                return 0
            if s == n:
                return 1
            if dp[s] != -1:
                return dp[s]
            dp[s] = backtrack(s + 1) + backtrack(s + 2)
            return dp[s]
        return backtrack(0)
        