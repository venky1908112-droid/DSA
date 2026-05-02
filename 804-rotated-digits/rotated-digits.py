class Solution:
    m = 10000 
    dp = [0] * (m+1)
    good = 0
    
    for i in range(1, m + 1):
        dp[i] = dp[i-1]
        x = i
        valid = True
        change = False

        while x > 0:
            d = x % 10

            if d in (3, 4, 7):
                valid = False
                break
            
            if d in (2, 5, 6, 9):
                change = True
            
            x //= 10

        if valid and change:
                dp[i] += 1
        

    def rotatedDigits(self, n: int) -> int:
        return self.dp[n]