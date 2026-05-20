class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        seen = set()
        res = []
        common = 0
        for x, y in zip(a, b):
            if x in seen:
                common += 1
            seen.add(x)
            if y in seen:
                common += 1
            seen.add(y)
            res.append(common)
        return res