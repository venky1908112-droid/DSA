class ATM:

    def __init__(self):
        self.money = [0,0,0,0,0]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i,x in enumerate(banknotesCount):
            self.money[i] += x

    def withdraw(self, amount: int) -> List[int]:
        temp = []
        for i,x in enumerate([500,200,100,50,20]):
            m = min(amount // x, self.money[4-i])
            temp.append(m)
            amount -= m * x
        if amount != 0:
            return [-1]
        temp.reverse()
        for i in range(5):
            self.money[i] -= temp[i]
        return temp

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)