class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0
        state = [0] * (n+1)
        for i in range(n+1):
            if i < 10:
                if i == 0 or i == 1 or i == 8:
                    state[i] = 1
                elif i == 3 or i == 4 or i == 7:
                    state[i] = 0
                else:
                    state[i] = 2
                    good += 1
                
            else:
                last_digit = state[i % 10]
                left_part = state[i // 10]
                
                if left_part == 0 or last_digit == 0:
                    state[i] = 0
                elif left_part == last_digit == 1:
                    state[i] = 1
                
                else:
                    state[i] = 2
                    good += 1
        return good