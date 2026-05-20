class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        common = 0
        seen = set()
        res = []
        for i in range(len(a)):
            if a[i] in seen:
                common += 1
            seen.add(a[i])
            
            if b[i] in seen:
                common += 1
            
            seen.add(b[i])
            res.append(common)
        return res