class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0
        for i in range(len(nums)):
            if reached < i:
                return False
            reached = max(i + nums[i], reached)
        return True