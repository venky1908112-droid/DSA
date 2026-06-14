from collections import defaultdict
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.first = Node(0,0)
        self.last = Node(0,0)
        self.first.next = self.last
        self.last.prev = self.first
        self.mp = defaultdict(lambda : None)
    
    def insert(self, key, value):
        node = Node(key, value)
        self.mp[key] = node
        node.prev = self.first
        node.next = self.first.next
        self.first.next.prev = node
        self.first.next = node

    def recently_used(self, key):
        node = self.mp[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.first
        node.next = self.first.next
        self.first.next.prev = node
        self.first.next = node
    
    def remove_lru(self):
        node = self.last.prev
        node.prev.next = self.last
        del self.mp[node.key]
        self.last.prev = node.prev
        del node

class LRUCache:

    def __init__(self, capacity: int):
        self.ll = DLL()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.ll.mp:
            return -1
        self.ll.recently_used(key)
        return self.ll.mp[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.ll.mp:
            self.ll.insert(key, value)
            if len(self.ll.mp) > self.size:
                self.ll.remove_lru()
        else:
            self.ll.mp[key].val = value
            self.ll.recently_used(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)