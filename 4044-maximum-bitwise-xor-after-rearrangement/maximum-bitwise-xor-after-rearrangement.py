class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        one_count = t.count('1')
        zero_count = len(t) - one_count
        res = ""
        for i in range(len(s)):
            if s[i] == '0':
                if one_count > 0:
                    one_count -= 1
                    res += '1'
                else:
                    for x in s[i:]:
                        res += '0' if x == '0' else '1'
                    break
            else:
                if zero_count > 0:
                    zero_count -= 1
                    res += '1'
                else:
                    for x in s[i:]:
                        res += '0' if x == '1' else '1'
                    break
        return res