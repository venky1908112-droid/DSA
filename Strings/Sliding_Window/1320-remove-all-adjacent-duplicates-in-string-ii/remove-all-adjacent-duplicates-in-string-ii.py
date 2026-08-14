class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for x in s:
            if not stack or stack[-1][0] != x:
                stack.append([x, 1])
                continue
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        res = ''
        for x, y in stack:
            res += x * y
        return res