# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        p1 = list1
        p2 = list2
        dummy = ListNode(0)
        temp = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                temp.next = p1
                temp = temp.next
                p1 = p1.next
            else:
                temp.next = p2
                temp = temp.next
                p2 = p2.next
        while p1:
            temp.next = p1
            p1 = p1.next
            temp = temp.next
        while p2:
            temp.next = p2
            p2 = p2.next
            temp = temp.next
        temp.next = None
        return dummy.next