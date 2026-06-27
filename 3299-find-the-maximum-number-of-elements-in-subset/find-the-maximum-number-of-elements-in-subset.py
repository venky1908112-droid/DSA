from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        one_count = freq[1]
        if not one_count & 1:
            one_count -= 1
        ans = one_count
        del freq[1]
        curr_ans = 0
        for key, val in freq.items():
            curr_ans = 0
            x = key
            while x in freq and freq[x] > 1:
                x = x * x
                curr_ans += 2
            ans = max(ans, curr_ans + (1 if x in freq else -1))
        return ans