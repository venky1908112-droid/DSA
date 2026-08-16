class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def idx(ch):
            if 'A' <= ch <= 'Z':
                return ord(ch) - 65
            return ord(ch) - 97 + 26
        res = ""
        left = 0
        req = [0] * 52
        window = [0] * 52
        length = 0
        for x in t:
            req[idx(x)] += 1
        for right in range(len(s)):
            pos = idx(s[right])
            window[pos] += 1
            if req[pos] >= window[pos]:
                length += 1
            if length < len(t):
                continue
            curr= idx(s[left])
            while window[curr] > req[curr]:
                window[curr] -= 1
                left += 1
                curr = idx(s[left])
            if not res or len(res) > (right - left + 1):
                res = s[left : right + 1]
        return res