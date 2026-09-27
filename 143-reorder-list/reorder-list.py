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

        prev = None
        curr = second
        while curr:
            next_link = curr.next
            curr.next = prev
            prev = curr
            curr = next_link
        
        second = prev


        first = head

        dummy = ListNode(0)
        temp = dummy

        while first or second:
            if first:
                temp.next = first
                first = first.next
                temp = temp.next
            
            if second:
                temp.next = second
                second = second.next
                temp = temp.next
        
