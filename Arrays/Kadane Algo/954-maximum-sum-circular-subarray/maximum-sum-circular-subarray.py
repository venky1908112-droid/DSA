class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr_min = nums[0]
        min_sum = nums[0]
        max_sum = nums[0]
        curr_max = nums[0]
        for x in nums[1:]:
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)
        if max_sum <= 0:
            return max_sum
        return max(total_sum - min_sum, max_sum)
