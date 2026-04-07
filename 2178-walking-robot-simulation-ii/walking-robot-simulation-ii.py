class Robot:

    def __init__(self, width: int, height: int):
        self.x_limit = width
        self.y_limit = height
        self.x = 0
        self.y = 0
        self.curr_d = 'East'

    def step(self, n: int) -> None:
        perimeter = 2 * (self.x_limit + self.y_limit) - 4
        if n % perimeter == 0:
            n = perimeter
        else:
            n %= perimeter
        while n > 0:
            if self.curr_d == 'East' and self.x + n >= self.x_limit:
                self.curr_d = 'North'
                n -= (self.x_limit - 1) - self.x
                self.x = self.x_limit - 1
            elif self.curr_d == 'North' and self.y + n >= self.y_limit:
                self.curr_d = 'West'
                n -= (self.y_limit - 1) - self.y
                self.y = self.y_limit - 1
            elif self.curr_d == 'West' and (self.x - n) < 0:
                self.curr_d = 'South'
                n -= self.x
                self.x = 0
            elif self.curr_d == 'South' and (self.y - n) < 0:
                self.curr_d = 'East'
                n -= self.y
                self.y = 0
            else:
                break
        if n != 0:
            if self.curr_d == 'East':
                self.x += n
            elif self.curr_d == 'North':
                self.y += n
            elif self.curr_d == 'West':
                self.x -= n
            else:
                self.y -= n


    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.curr_d


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()