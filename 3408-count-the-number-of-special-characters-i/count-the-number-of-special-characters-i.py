class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        vals = set(word)
        special = 0
        for letter in vals:
            if 'a' <= letter <= 'z':
                #uppercase
                if chr(ord(letter) - 32) in vals:
                    special += 1
            else:
                #lowercase        
                if chr(ord(letter) + 32) in vals:
                    special += 1
        return special // 2