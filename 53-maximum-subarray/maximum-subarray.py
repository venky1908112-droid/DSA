class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        mx_sum = float('-inf')
        for x in nums:
            s += x
            mx_sum = max(mx_sum, s)
            if s < 0:
                s = 0
        return mx_sum