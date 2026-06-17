class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = [0]

        # Store length after each operation
        for ch in s:
            curr = lengths[-1]

            if ch == '*':
                lengths.append(max(0, curr - 1))
            elif ch == '#':
                lengths.append(curr * 2)
            elif ch == '%':
                lengths.append(curr)
            else:
                lengths.append(curr + 1)

        # k is 0-indexed
        if k >= lengths[-1]:
            return '.'

        target = k

        # Trace the target index backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            before = lengths[i]

            if ch == '#':
                # before: ABC
                # after : ABCABC
                if target >= before:
                    target -= before

            elif ch == '%':
                # before: ABCDE
                # after : EDCBA
                target = before - 1 - target

            elif ch == '*':
                # before: ABCD
                # after : ABC
                # surviving indices stay the same
                pass

            else:
                # before: ABC
                # after : ABCx
                # x is added at index 'before'
                if target == before:
                    return ch

        return '.'