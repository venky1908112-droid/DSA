class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        mn = float('inf')
        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                mn = min(mn, min(d,n - d))
        return mn if mn != float('inf') else -1
