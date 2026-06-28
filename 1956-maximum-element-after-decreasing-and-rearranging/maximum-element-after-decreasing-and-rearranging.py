class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        op = 0
        if sorted(arr) != arr:
            arr.sort()
            op = 1
        n = len(arr)
        if n == 1:
            return 1
        arr[0] = 1
        m = 0
        for i in range(1,n):
            if (arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i - 1] + 1
            m = max(m, arr[i])
        return m

        