class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]
        for x in nums[1:]:
            if x < 0:
                curr_max , curr_min = curr_min, curr_max
            curr_max = max(x, curr_max * x)
            curr_min = min(x, curr_min * x)
            ans = max(ans, curr_max)
        return ans