class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = []
        def isodd(n):
            return n & 1
        for i in range(n):
            count = 0
            for j  in range(n - 1, i - 1, -1):
                if isodd(nums[i]) != isodd(nums[j]):
                    count += 1
            res.append(count)

        return res
            