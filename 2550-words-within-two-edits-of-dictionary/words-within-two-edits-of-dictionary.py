class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            for d in dictionary:
                if sum(1 for a,b in zip(query, d) if a != b) <= 2:
                    res.append(query)
                    break
        return res