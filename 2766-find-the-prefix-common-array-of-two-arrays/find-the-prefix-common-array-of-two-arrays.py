from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        visited = [0] * (len(a) + 1)
        res = []
        common= 0
        for x, y in zip(a, b):
            if visited[x] == 1:
                common += 1
            visited[x] += 1
            if visited[y] == 1:
                common += 1
            visited[y] += 1
            res.append(common)
        return res