from collections import Counter
class Solution(object):
    def mirrorFrequency(self, s):
        visited = set()
        ans = 0
        freq = Counter(s) # key , value = value, freq 
        for c in freq:
            # only keys
            if c in visited:
                continue
            if c.isdigit():
                m = str(9 - int(c))
            else:
                m = chr(219 - ord(c))
            ans += abs(freq[c] - freq.get(m,0))
            visited.add(c)
            visited.add(m)
        return ans