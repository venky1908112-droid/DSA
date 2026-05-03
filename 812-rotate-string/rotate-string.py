class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        n = len(s)
        for i in range(n):
            equal = True
            for j in range(n):
                if s[(i + j) % n] != goal[j % n]:
                    equal = False
                    break
            if equal:
                return True
        return False