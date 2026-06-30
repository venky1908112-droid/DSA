from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        n = len(s)
        mp = defaultdict(int)
        ans = 0
        for right in range(n):
            mp[s[right]] += 1
            while len(mp) >= 3:
                ans += n - right
                mp[s[left]] -= 1
                if mp[s[left]] == 0:
                    del mp[s[left]]
                left += 1
        return ans