class Solution:
    def reverseParentheses(self, s: str) -> str:
        open = 0
        stack = []
        res = ""
        for ch in s:
            if ch == '(':
                open += 1
                stack.append(ch)
            elif ch == ')':
                s2 = []
                open -= 1
                while stack and stack[-1] != '(':
                    s2.append(stack.pop())
                stack.pop()
                if stack:
                    for x in s2:
                        stack.append(x)
                else:
                    res += ''.join(s2)
            elif open > 0:
                stack.append(ch)
            else:
                res += ch
        return res