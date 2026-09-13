class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = prev_rob = 0
        for curr_val in nums:
            temp = max(max_rob, prev_rob + curr_val)
            prev_rob = max_rob
            max_rob = temp
        return max_rob
