class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        chances = 0
        mx_len = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if chances < k:
                    chances += 1
                else:
                    while nums[left] == 1:
                        left += 1
                    left += 1
            mx_len = max(mx_len, right - left + 1)
        return mx_len