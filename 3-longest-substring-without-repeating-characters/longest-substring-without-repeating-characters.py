class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        mx_len = 0
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            mx_len = max(mx_len , right - left + 1)
        return mx_len
            