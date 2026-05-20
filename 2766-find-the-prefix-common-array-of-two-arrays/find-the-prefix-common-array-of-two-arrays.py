class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        bit = 0
        common = 0
        res = []
        for i in range(len(a)):
            x, y = a[i], b[i]
            if (bit >> x) & 1:
                common += 1
            else:
                bit |= (1 << x)

            if (bit >> y) & 1:
                common += 1
            else:
                bit |= (1 << y)
            res.append(common)
        return res