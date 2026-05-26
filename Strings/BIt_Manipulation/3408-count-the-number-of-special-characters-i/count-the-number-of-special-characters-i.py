class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = 0
        upper = 0
        for letter in word:
            if 'a' <= letter <= 'z':
                lower |= 1 << (ord(letter) - 97)
            else:
                upper |= 1 << (ord(letter) - 65)
        return (lower & upper).bit_count()