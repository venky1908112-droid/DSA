class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = [-1] * 26
        for i, x in enumerate(s):
            last[ord(x) - ord('a')] = i
        visited = [False] * 26
        stack = []
        for i, x in enumerate(s):
            idx = ord(x) - ord('a')

            if visited[idx]:
                continue
            
            while stack and stack[-1] > x and last[ord(stack[-1]) - ord('a')] > i:
                visited[ord(stack.pop()) - ord('a')] = False

            stack.append(x)
            visited[idx] = True
        return ''.join(stack)