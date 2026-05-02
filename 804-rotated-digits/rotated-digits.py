class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0] * (n+1)
        good = 0
        for i in range(n + 1):
            if i < 10:
                if i in (0, 1, 8):
                    dp[i] = 1
                elif i in (2, 5, 6, 9):
                    dp[i] = 2
                    good += 1
                else:
                    continue
            else:
                left = dp[i // 10]
                last_digit = dp[i % 10]
                if left == 0 or last_digit == 0:
                    dp[i] = 0
                elif left == 1 and last_digit == 1:
                    dp[i] = 1
                else:
                    dp[i] = 2
                    good += 1

        return good
