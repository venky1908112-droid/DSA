from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        idx_sum = defaultdict(int)
        for i, n in enumerate(nums):
            d[n].append(i)
            idx_sum[n] += i
        res = [0] * len(nums)
        for val, idx_list in d.items():
            prefix_sum = 0
            s = idx_sum[val]
            n = len(idx_list)
            for i, idx in enumerate(idx_list):
                res[idx] += i * idx - prefix_sum
                prefix_sum += idx
                res[idx] += (s - prefix_sum) - (idx * (n - i - 1))
        return res