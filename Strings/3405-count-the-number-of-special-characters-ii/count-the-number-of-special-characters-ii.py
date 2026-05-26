class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = 0
        lowercase = {}
        uppercase = {}
        visited = set()
        for i, letter in enumerate(word):
            if 'a' <= letter <= 'z':
                lowercase[letter] = i
            else:
                if letter not in visited:
                    uppercase[letter] = i
                    visited.add(letter)
        for character, index in uppercase.items():
            lwr = chr(ord(character) + 32)
            if lwr not in lowercase:
                continue
            if lowercase[lwr] < index:
                special += 1
        return special

