import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            product = 1
            hcf = 0
            lcm = 1
            for j in range(i,n):
                product *= nums[j]
                hcf = math.gcd(nums[j], hcf)
                lcm = math.lcm(nums[j], lcm)
                if product == lcm * hcf:
                    max_len = max(max_len, j - i + 1)
        return max_len