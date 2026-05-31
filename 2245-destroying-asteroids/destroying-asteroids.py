class Solution:
    def asteroidsDestroyed(self, mass: int, a: List[int]) -> bool:
        a.sort()
        for x in a:
            if mass >= x:
                mass += x
            else:
                return False
        return True