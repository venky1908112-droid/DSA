class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = 0
        lowercase = {}
        uppercase = {}
        for i, letter in enumerate(word):
            if 'a' <= letter <= 'z':
                lowercase[letter] = i
        for i in range(len(word)- 1, -1, -1):
            uppercase[word[i]] = i
        for character, index in uppercase.items():
            lwr = chr(ord(character) + 32)
            if lwr not in lowercase:
                continue
            if lowercase[lwr] < index:
                special += 1
        return special

