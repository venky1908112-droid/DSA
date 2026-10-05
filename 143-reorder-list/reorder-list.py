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
        a = []
        temp = head
        while temp:
            a.append(temp)
            temp = temp.next
        
        left = 0
        right = len(a) - 1

        while left < right:
            a[left].next = a[right]
            left += 1

            if left < right:
                a[right].next = a[left]
                right -= 1

        a[left].next = None