from collections import defaultdict

class Solution(object):
    def findGoodIntegers(self, n):
        cube_count = defaultdict(int)
        
        a = 1
        while a**3 <= n:
            b = a
            while a**3 + b**3 <= n:
                x = a**3 + b**3
                cube_count[x] += 1
                b += 1
            a += 1
        
        ans = []
        for num in cube_count:
            if cube_count[num] >= 2:
                ans.append(num)
        
        return sorted(ans)