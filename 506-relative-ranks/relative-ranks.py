import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = []
        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))
        res = [""] * n
        rank = 1
        while heap:
            s, idx = heapq.heappop(heap)
            if rank == 1:
                res[idx] = "Gold Medal"
            elif rank == 2:
                res[idx] = "Silver Medal"
            elif rank == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank)
            rank += 1
        return res
            
