class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        seen = [0] * (n + 1)
        common = 0
        res = []
        for i in range(n):
            seen[a[i]] += 1
            if seen[a[i]] == 2:
                common += 1
            seen[b[i]] += 1
            if seen[b[i]] == 2:
                common += 1
            res.append(common)
        return res