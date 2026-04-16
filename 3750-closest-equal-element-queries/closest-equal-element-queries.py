from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
        res = [-1] * len(queries)
        for i,query in enumerate(queries):
            n = len(d[nums[query]])
            if n > 1:
                mn = float('inf')
                lst = d[nums[query]]
                left = 0
                right = n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if lst[mid] == query:
                        if mid > 0:
                            dist = lst[mid] - lst[mid - 1]
                            mn = min(mn, dist, len(nums) - dist)
                        else:
                            dist = lst[-1] - lst[mid]
                            mn = min(mn, dist, len(nums) - dist)
                        if mid < n - 1:
                            dist = lst[mid + 1] - lst[mid]
                            mn = min(mn, dist, len(nums) - dist)
                        else:
                            dist = lst[mid] - lst[0]
                            mn = min(mn, dist, len(nums) - dist)
                        res[i] = mn
                        break
                    if lst[mid] < query:
                        left = mid + 1
                    else:
                        right = mid - 1
                
        return res
        