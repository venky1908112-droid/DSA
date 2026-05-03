class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        odd_count = even_count = 0
        for i in range(n - 1 , -1, -1):
            if nums[i] & 1:
                res[i] = even_count
                odd_count += 1
            else:
                res[i] = odd_count
                even_count += 1
        return res