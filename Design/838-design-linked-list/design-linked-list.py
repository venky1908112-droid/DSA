class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        if index >= self.length:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        if index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        prev = None
        curr = self.head
        while index:
            prev = curr
            curr = curr.next
            index -= 1
        prev.next = new_node
        new_node.next = curr
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index >= self.length:
            return 
        if index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            prev = None
            curr = self.head
            while index:
                index -= 1
                prev = curr
                curr = curr.next
            temp = curr
            curr = curr.next
            prev.next = curr
        self.length -= 1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)