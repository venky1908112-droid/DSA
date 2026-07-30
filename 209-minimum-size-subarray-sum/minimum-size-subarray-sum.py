class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')
        s = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                min_length = min(right - left + 1, min_length)
                s -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length