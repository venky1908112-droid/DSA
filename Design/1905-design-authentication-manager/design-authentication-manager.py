from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = defaultdict(int)
        self.alive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.alive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return 
        if self.tokens[tokenId] <= currentTime:
            del self.tokens[tokenId]
        else:
            self.tokens[tokenId] = currentTime + self.alive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key, val in list(self.tokens.items()):
            if val > currentTime:
                count += 1
            else:
                del self.tokens[key]
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)