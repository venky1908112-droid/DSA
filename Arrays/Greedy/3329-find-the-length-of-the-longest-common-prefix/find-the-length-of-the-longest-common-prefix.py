class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        possible = set()
        for x in arr1:
            while x > 0:
                possible.add(x)
                x //= 10
        longest = 0
        for x in arr2:
            while x > 0:
                if x in possible:
                    longest = max(longest, len(str(x)))
                    break
                x //= 10
        return longest