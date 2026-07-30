class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')

        s = 0
        left = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                min_length = min(min_length, right - left + 1)
                s -= nums[left]
                left += 1


        return 0 if min_length == float('inf') else min_length