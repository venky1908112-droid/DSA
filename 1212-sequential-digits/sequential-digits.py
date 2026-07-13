class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = '123456789'
        s_l = len(str(low))
        e_l = len(str(high))
        for length in range(s_l, e_l + 1):
            for start in range(10 - length):
                num = int(digits[start : start + length])
                if low <= num <= high:
                    result.append(num)
        return result
