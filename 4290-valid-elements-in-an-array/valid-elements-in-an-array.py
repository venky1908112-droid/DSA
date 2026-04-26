class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        if n == 1:
            return [nums[0]]
        
        # Precompute left max
        left_max = [float('-inf')] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i-1])
        
        # Precompute right max
        right_max = [float('-inf')] * n
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i+1])
        
        res = []
        
        for i in range(n):
            if nums[i] > left_max[i] or nums[i] > right_max[i]:
                res.append(nums[i])
        
        return res