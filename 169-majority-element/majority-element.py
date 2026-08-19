class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = -1
        for x in nums:
            if count == 0:
                ans = x
                count = 1
            elif x == ans:
                count += 1
            else:
                count -= 1
        return ans