class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x > 9:
                for v in str(x):
                    res.append(int(v))
            else:
                res.append(x)
        return res