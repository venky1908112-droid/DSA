from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        one_count = freq[1]
        if one_count % 2 == 0:
            one_count -= 1
        ans = one_count
        del freq[1]
        for key, val in freq.items():
            curr_ans = 0
            x = key
            while x in freq and freq[x] > 1:
                curr_ans += 2
                x = x * x
            ans = max(ans, curr_ans + (1 if x in freq else -1))
        return ans