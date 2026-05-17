class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = set()
        def dfs(i):
            if i < 0 or i >= n or i in seen:
                return False
            if arr[i] == 0:
                return True
            seen.add(i)
            return dfs(i - arr[i]) or dfs(i + arr[i])
        return dfs(start)