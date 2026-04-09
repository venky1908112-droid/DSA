from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [""] * n
        sorted_idx = sorted(range(n), key=lambda i: score[i], reverse=True)
        
        for rank, idx in enumerate(sorted_idx):
            if rank == 0:
                res[idx] = "Gold Medal"
            elif rank == 1:
                res[idx] = "Silver Medal"
            elif rank == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank + 1)
        
        return res