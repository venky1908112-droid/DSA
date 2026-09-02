class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0
            
        max_reach = 0
        curr_end = 0
        jumps = 0
        
        for i in range(n):
            max_reach = max(max_reach , i + nums[i])

            if curr_end == i:
                jumps += 1
                curr_end = max_reach

                if curr_end >= n - 1:
                    break
        return jumps