class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        vals = set(word)
        special = 0
        for letter in vals:
            if 'a' <= letter <= 'z':
                if chr(ord(letter) - 32) in vals:
                    special += 1
        return special
