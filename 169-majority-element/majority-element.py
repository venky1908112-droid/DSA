from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key, val in freq.items():
            if val > len(nums) // 2:
                return key