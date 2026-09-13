class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = -1
        count = 0
        for x in nums:
            if count == 0:
                val = x
                count = 1
            elif val == x:
                count += 1
            else:
                count -= 1
        return val