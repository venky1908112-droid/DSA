class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        underscore = 0
        for x in moves:
            if x == 'L':
                left += 1
            elif x == 'R':
                right += 1
            else:
                underscore += 1
        return abs(left - right) + underscore 