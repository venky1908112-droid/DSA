class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left = 0
        right = n - 1
        for i in range(n):
            if colors[i] != colors[-1]:
                left = i
                break
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                right = i
                break
        return max(right, n -1 - left)