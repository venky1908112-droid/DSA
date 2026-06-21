class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        count = [0] * (max_val + 1)
        for x in costs:
            count[x] += 1
        ans = 0
        for price, x in enumerate(count):
            if x == 0:
                continue
            if coins < price:
                break
            buy = min(coins // price, x)
            ans += buy 
            coins -= buy * price

        return ans