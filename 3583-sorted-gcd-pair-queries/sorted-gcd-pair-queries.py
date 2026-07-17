class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        gcd = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            t_pairs = (sm * (sm - 1)) // 2
            gcd[i] = t_pairs - sum(gcd[i::i])
        prefix = list(accumulate(gcd))
        res = []
        for q in queries:
            res.append(bisect.bisect_right(prefix, q))
        return res
            

        
