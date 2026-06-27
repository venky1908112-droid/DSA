class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        amount = 0
        for i in range(len(cost)):
            if (i + 1) % 3 == 0:
                continue
            else:
                amount += cost[i]
        return amount