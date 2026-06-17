class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = [0]
        for x in s:
            curr = length[-1]
            if x == '*':
                length.append(curr - 1 if curr > 0 else 0)
            elif x == '#':
                length.append(curr * 2)
            elif x == '%':
                length.append(curr)
            else:
                length.append(curr + 1)
        if k >= length[-1]:
            return '.'
        target = k
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == '*':
                pass
            elif ch == '#':
                if target >= length[i]:
                    target -= length[i]
            elif ch == '%':
                target = length[i] - 1 - target
            else:
                if target == length[i]:
                    return ch
        return '.'