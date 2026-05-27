class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = {}
        for i, letter in enumerate(word):
            if 'a' <= letter <= 'z':
                lowercase[letter] = i
        uppercase = {}
        for i in range(len(word) - 1,  - 1, - 1):
            if 'A' <= word[i] <= 'Z':
                uppercase[word[i]] = i
        special = 0
        for letter, index in uppercase.items():
            if letter.lower() not in lowercase:
                continue
            if lowercase[letter.lower()] < index:
                special += 1
        return special
        
