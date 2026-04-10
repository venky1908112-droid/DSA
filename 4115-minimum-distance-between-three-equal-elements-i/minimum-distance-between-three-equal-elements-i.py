class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        mn = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j + 1,n):
                    if nums[i] == nums[j] == nums[k]:
                        mn = min(mn, abs(i - j) + abs(j - k) + abs(k - i))
        return -1 if mn == float('inf') else mn