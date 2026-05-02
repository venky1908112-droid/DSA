class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0

        for i in range(1, n + 1):
            x = i
            valid = True
            change = False

            while x > 0:
                d = x % 10

                if d in (3, 4, 7):
                    valid = False
                    break
                
                if d in (2, 5, 6, 9):
                    change = True
                
                x //= 10

            if valid and change:
                good += 1
        return good