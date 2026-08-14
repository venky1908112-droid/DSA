class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = -1
        for val in nums:
            if count == 0:
                ans = val
                count = 1
            elif val == ans:
                count += 1
            else:
                count -= 1
        return ans