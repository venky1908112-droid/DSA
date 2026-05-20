class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        s = 0
        res = []
        common= 0
        for x, y in zip(a, b):
            if (s >> x) & 1: 
                common += 1
            else:
                s |= (1 << x)
            if (s >> y) & 1: 
                common += 1
            else:
                s |= (1 << y)
            res.append(common)
        return res