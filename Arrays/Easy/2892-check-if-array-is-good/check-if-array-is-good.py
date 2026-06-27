class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        c = 1
        for x in nums[:-1]:
            if x != c:
                return False
            c += 1
        return nums[-1] == len(nums) - 1
        

