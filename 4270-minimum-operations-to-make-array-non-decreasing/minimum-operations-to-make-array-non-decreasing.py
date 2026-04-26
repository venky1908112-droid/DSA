class Solution:
    def minOperations(self, nums):
        cost = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                cost += nums[i - 1] - nums[i]
        
        return cost