class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0
        m = len(nums1)
        n = len(nums2)
        mx = 0
        while p1 < m and p2 < n:
            if nums1[p1] > nums2[p2]:
                p1 += 1
            else:
                mx = max(mx, p2 - p1)
                p2 += 1
            if p2 < p1:
                p2 += 1
        return mx