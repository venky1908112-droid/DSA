class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        tank = 0
        start = 0
        for i in range(n):
            balance = gas[i] - cost[i]
            total += balance
            tank += balance
            if tank < 0:
                start = i + 1
                tank = 0
        if total < 0:
            return -1
        return start