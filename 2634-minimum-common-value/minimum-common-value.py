class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if not common:
            return -1
        return min(common)