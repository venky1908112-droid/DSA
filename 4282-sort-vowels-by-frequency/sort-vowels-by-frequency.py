from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        d = defaultdict(int)
        vowels = ['a','e','i','o','u'] 
        for x in s:
            if x in vowels:
                d[x] += 1
        items = list(d.items())
        items.sort(key = lambda x: x[1], reverse = True)
        sorted_vowels = []
        #[e,e,e,o]
        for ch, freq in items:
            sorted_vowels.extend([ch] * freq)
        p = 0
        res = ""
        for x in s:
            if x in vowels:
                res += sorted_vowels[p]
                p += 1
            else:
                res += x
        return res