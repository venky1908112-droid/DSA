class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        
        i = 0
        while i < n - 1 and nums[i] <= nums[i + 1]:
            i += 1
        
        for j in range(i + 1,i + n):
            curr = j % n
            nxt = (j + 1) % n
            if nums[curr] > nums[nxt]:
                return False
        
        return True