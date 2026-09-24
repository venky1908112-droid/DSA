# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        if l == n:
            temp = head
            head = head.next
            del temp
        else:
            temp = head
            prev = None
            for _ in range(l - n):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            del temp
        return head