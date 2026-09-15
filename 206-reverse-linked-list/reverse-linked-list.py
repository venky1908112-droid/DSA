# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = head
        while curr:
            temp = dummy.next
            dummy.next = curr
            curr = curr.next
            dummy.next.next = temp
        return dummy.next