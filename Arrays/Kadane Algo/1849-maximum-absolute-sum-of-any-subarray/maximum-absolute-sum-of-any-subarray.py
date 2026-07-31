class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        min_sum = nums[0]
        max_sum = nums[0]
        for x in nums[1:]:
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum , curr_max)
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)
        return max(max_sum , abs(min_sum))


