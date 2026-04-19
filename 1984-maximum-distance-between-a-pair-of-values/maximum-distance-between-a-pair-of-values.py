class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        mx = 0
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                mx = max(mx, j - i)
                j += 1
            else:
                i += 1
            if i > j:
                j += 1
        return mx
            
