class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x : x[1] - x[0])
        energy = 0
        for a,m in tasks:
            energy = max(energy + a, m)
        return energy