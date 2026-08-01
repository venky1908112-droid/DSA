from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        mx_len = 0
        mx_freq = 0
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            mx_freq = max(mx_freq, window[s[right]])
            while ((right - left + 1) - mx_freq) > k:
                window[s[left]] -= 1
                left += 1
            mx_len = max(mx_len, right - left + 1)
        return mx_len