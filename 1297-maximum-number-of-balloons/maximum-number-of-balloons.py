class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b' : 0, 'a' : 0, 'l' : 0, 'o' : 0, 'n' : 0}
        for x in text:
            if x in 'balon':
                d[x] += 1
        ans = float('inf')
        for key, val in d.items():
            if key in 'lo':
                val //= 2
            ans = min(ans, val)
        return ans