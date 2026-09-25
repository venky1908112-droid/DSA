# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        dummy = ListNode(0)
        curr = second
        while curr:
            t = dummy.next
            dummy.next = curr
            curr = curr.next
            dummy.next.next = t
        second = dummy.next

        first = head

        dummy.next = None

        temp = dummy

        while first or second:
            if first:
                temp.next = first
                temp = temp.next
                first = first.next
            if second:
                temp.next = second
                temp = temp.next
                second = second.next
                
        return dummy.next
        