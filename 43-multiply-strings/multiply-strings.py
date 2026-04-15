class Solution(object):
    def multiply(self, num1, num2):
        d  = {
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '0' : 0
        }
        v1 = 0
        for n in num1:
            v1 = v1 * 10 + d[n]
        v2 = 0
        for n in num2:
            v2 = v2 * 10 + d[n]
        return str(v1 * v2)