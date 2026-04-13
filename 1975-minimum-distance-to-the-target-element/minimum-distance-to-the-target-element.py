class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mn = float('inf')
        for i,x in enumerate(nums):
            if x == target:
                mn = min(mn, abs(i - start))
        return mn