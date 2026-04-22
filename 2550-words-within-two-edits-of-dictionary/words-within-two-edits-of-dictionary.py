class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def difference(s1, s2):
            d = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    d += 1
                if d > 2:
                    return False
            return True
        res = []
        for query in queries:
            for d in dictionary:
                if difference(query, d):
                    res.append(query)
                    break
        return res