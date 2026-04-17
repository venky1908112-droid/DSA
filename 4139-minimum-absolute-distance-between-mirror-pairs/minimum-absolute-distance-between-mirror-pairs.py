class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mn_diff = float('inf')
        visited = {}
        for i, val in enumerate(nums):
            if val in visited:
                mn_diff = min(mn_diff, i - visited[val])
            visited[int(str(val)[::-1])] = i
        return mn_diff if mn_diff != float('inf') else -1