class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        n = len(t)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and stack[-1][0] < t[i]:
                v, j = stack.pop()
                res[j] = i - j
            stack.append((t[i], i))
        return res