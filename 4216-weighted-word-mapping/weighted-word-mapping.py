class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = str()
        for word in words:
            total = sum(weights[ord(ch) - 97] for ch in word)
            result += chr(122 - total % 26)
        return result