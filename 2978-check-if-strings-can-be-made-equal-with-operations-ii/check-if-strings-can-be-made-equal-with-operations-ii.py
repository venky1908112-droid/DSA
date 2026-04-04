from collections import defaultdict
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd = defaultdict(int)
        even = defaultdict(int)
        for i in range(len(s1)):
            if i & 1:
                odd[s1[i]] += 1
            else:
                even[s1[i]] += 1
        for i in range(len(s2)):
            if i & 1:
                if odd[s2[i]] > 0:
                    odd[s2[i]] -= 1
                else:
                    return False
            else:
                if even[s2[i]] > 0:
                    even[s2[i]] -= 1
                else:
                    return False
        return True