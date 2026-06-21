class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        count = [0] * (max_val + 1)
        for x in costs:
            count[x] += 1
        ans = 0
        for price, freq in enumerate(count):
            if freq == 0:
                continue
            if coins < price:
                break
            buy = min(coins // price, freq)
            ans += buy
            coins -= buy * price
        return ans