class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        res = []
        for x, y in zip(a, b):
            s1.add(x)
            s2.add(y)
            res.append(len(s1 & s2))
        return res