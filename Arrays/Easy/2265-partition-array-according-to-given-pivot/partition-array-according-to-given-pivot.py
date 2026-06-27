class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small =[]
        pvt = []
        large = []
        for x in nums:
            if x < pivot:
                small.append(x)
            elif x == pivot:
                pvt.append(x)
            else:
                large.append(x)
        return small + pvt + large