class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        amount = 0
        n = len(cost)
        if n <= 2:
            return sum(cost)
        cost.sort(reverse = True)
        for i in range(n):
            if (i + 1) % 3 == 0:
                continue
            else:
                amount += cost[i]
        return amount