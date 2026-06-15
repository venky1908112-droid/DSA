# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        if length == 1:
            del head
            return None
        temp = head
        prev = None
        for _ in range(length // 2):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp
        return head