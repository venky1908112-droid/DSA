class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = 0
        lowercase = {}
        uppercase = {}
        visited = 0
        for i, letter in enumerate(word):
            if 'a' <= letter <= 'z':
                lowercase[letter] = i
            else:
                if not (visited >> (ord(letter) - 65)) & 1:
                    uppercase[letter] = i
                    visited |= 1 << (ord(letter) - 65)
        for character, index in uppercase.items():
            lwr = chr(ord(character) + 32)
            if lwr not in lowercase:
                continue
            if lowercase[lwr] < index:
                special += 1
        return special

