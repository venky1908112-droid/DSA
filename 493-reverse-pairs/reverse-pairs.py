class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, low, mid, high):
            pairs = 0
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] > nums[right] * 2:
                    pairs += mid + 1 - left
                    right += 1
                else:
                    left += 1
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= high:
                temp.append(nums[right])
                right += 1
            for i in range(low, high + 1):
                nums[i] = temp[i - low]
            return pairs


        def mergesort(nums, low, high):
            pairs = 0
            if low >= high:
                return 0
            mid = (low + high) // 2
            pairs += mergesort(nums, low, mid)
            pairs += mergesort(nums, mid + 1, high)
            pairs += merge(nums, low, mid, high)
            return pairs
        
        return mergesort(nums, 0, len(nums) - 1)
