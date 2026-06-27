class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            c = 0
            for j in range(i, n):
                c += 1 if nums[j] == target else -1
                if c > 0:
                    ans += 1
        return ans