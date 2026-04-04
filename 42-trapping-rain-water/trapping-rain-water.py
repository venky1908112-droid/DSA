class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax, rmax = 0, 0
        water = 0
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax < rmax:
                water += lmax - height[left]
                left += 1
            else:
                water += rmax - height[right]
                right -= 1
        return water