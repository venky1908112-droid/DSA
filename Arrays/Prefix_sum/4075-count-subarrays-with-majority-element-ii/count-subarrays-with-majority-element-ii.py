class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        freq_count = [0] * (2 * n + 1)
        freq_count[n] = 1
        ans = 0
        prev_subarrays = 0
        count = n
        for i in range(n):
            if nums[i] == target:
                prev_subarrays += freq_count[count]
                count += 1
            else:
                count -= 1
                prev_subarrays -= freq_count[count]
            ans += prev_subarrays
            freq_count[count] += 1
        return ans
