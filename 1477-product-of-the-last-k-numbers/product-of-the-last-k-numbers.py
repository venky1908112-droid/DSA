class ProductOfNumbers:

    def __init__(self):
        self.last_zero = -1
        self.prev_product = 1
        self.prefix = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix.append(self.prev_product)
            self.last_zero = len(self.prefix) - 1
        else:
            curr = num * self.prev_product
            self.prefix.append(curr)
            self.prev_product = curr


    def getProduct(self, k: int) -> int:
        if k >= (len(self.prefix) - self.last_zero):
            return 0
        if k >= len(self.prefix):
            return self.prev_product
        return self.prev_product // self.prefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)