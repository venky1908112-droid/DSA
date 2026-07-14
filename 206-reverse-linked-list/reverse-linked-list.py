# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(curr):
            if not curr or not curr.next:
                return curr
            next_link = recursion(curr.next)
            curr.next.next = curr
            curr.next = None
            return next_link
        return recursion(head)