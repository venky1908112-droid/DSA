class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0
        for i in range(len(nums)):
            if i > reached:
                return False
            reached = max(reached, i + nums[i])
        return True