class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.n = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.n
        self.q[self.front] = value
        self.size += 1

        if self.size == 1:
            self.rear = self.front

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.n
        self.q[self.rear] = value
        self.size += 1

        if self.size == 1:
            self.front = self.rear

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.front] = -1
        self.front = (self.front + 1) % self.n
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.rear] = -1
        self.rear = (self.rear - 1) % self.n
        self.size -= 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.n