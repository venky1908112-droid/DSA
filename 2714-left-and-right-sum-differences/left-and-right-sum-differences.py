class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]
        suffix = [0] * n
        for i in range(1,n):
            prefix.append(prefix[i - 1] + nums[i - 1])
        for j in range(n - 2, -1 , -1):
            suffix[j] = suffix[j + 1] + nums[j + 1]
        ans = []
        for a, b in zip(prefix, suffix):
            ans.append(abs(a - b))
        return ans        