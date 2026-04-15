class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        left = right = 0
        left_done = right_done = False
        if target not in words:
            return -1
        for i in range(startIndex, startIndex + n):
            if words[i % n] != target:
                right += 1
            else:
                break
        for i in range(startIndex, startIndex - n, -1):
            if words[(i + n) % n] != target:
                left += 1
            else:
                break
                
        return min(right,left)