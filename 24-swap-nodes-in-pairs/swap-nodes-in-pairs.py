# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(curr):
            if not curr or not curr.next:
                return curr
            link = curr.next.next
            curr.next.next = curr
            prev_node = curr.next
            curr.next = recursion(link)
            return prev_node
        return recursion(head)