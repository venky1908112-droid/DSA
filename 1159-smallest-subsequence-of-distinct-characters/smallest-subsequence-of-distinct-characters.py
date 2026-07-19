class Solution:
    def smallestSubsequence(self, s: str) -> str:
        def c_t_i(c):
            return ord(c) - 97
        stack = []
        last_index = [-1] * 26
        for i,x in enumerate(s):
            last_index[ord(x) - 97] = i
        visited = [False] * 26
        for i, x in enumerate(s):
            if visited[c_t_i(x)]:
                continue

            while stack and last_index[c_t_i(stack[-1])] > i and stack[-1] > x:
                visited[c_t_i(stack.pop())] = False

            stack.append(x)
            visited[c_t_i(x)] = True
        return ''.join(stack)
        