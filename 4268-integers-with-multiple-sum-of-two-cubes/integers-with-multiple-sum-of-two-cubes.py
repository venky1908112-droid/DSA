from collections import defaultdict
class Solution(object):
    def findGoodIntegers(self, n):
        cube_pair = defaultdict(int)
        res = []
        a = 1
        while a ** 3 <= n:
            b = a
            while a ** 3 + b ** 3 <= n:
                x = a ** 3 + b ** 3
                cube_pair[x] += 1
                b += 1
            a += 1
        for key,val in cube_pair.items():
            if val >= 2:
                res.append(key)
        return sorted(res)
