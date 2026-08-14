class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        req = [0] * 26
        for x in p:
            req[ord(x) - 97] += 1
        left = 0
        ans = []
        window = [0] * 26
        for right in range(len(s)):
            idx = ord(s[right]) - 97
            window[idx] += 1
            while window[idx] > req[idx]:
                window[ord(s[left]) - 97] -= 1
                left += 1
            if (right - left + 1) == len(p):
                ans.append(left)
                window[ord(s[left]) - 97] -= 1
                left += 1
        return ans
