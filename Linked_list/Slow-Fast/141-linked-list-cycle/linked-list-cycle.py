# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = r = head
        while r and r.next:
            t = t.next
            r = r.next.next

            if t == r:
                return True
        
        return False