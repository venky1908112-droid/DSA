class Solution(object):
    def totalWaviness(self, num1, num2):
        count = 0
        for i in range(num1, num2 + 1):
            digits = list(map(int,str(i)))
            for a, b, c in zip(digits, digits[1:], digits[2:]):
                if (a < b > c) or (a > b < c):
                    count += 1
        return count 