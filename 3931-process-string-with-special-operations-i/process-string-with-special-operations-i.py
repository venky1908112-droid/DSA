class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == '#':
                result.extend(result)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '%':
                result.reverse()
            else:
                result.append(ch)
        return ''.join(result)