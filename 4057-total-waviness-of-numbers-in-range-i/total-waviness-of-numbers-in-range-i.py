class Solution(object):
    def totalWaviness(self, num1, num2):
        total = 0

        for num in range(num1, num2 + 1):
            digits = list(map(int, str(num)))

            for a, b, c in zip(digits, digits[1:], digits[2:]):
                if (a < b > c) or (a > b < c):
                    total += 1

        return total