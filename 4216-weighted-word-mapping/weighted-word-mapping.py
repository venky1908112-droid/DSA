class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = str()

        for word in words:
            total = sum(weights[ord(ch) - ord('a')] for ch in word)
            result += chr(ord('z') - total % 26)

        return result