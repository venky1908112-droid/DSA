class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp_no = 0
        component = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp_no += 1
            component[i] = comp_no
        res = []
        for u, v in queries:
            res.append(component[u] == component[v])
        return res