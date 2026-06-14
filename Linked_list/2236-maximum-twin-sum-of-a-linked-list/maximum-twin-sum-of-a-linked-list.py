# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        stack = []
        mx = 0
        temp = head
        for i in range(l):
            if i < (l // 2):
                stack.append(temp.val)
            else:
                mx = max(mx, stack.pop() + temp.val)
            temp = temp.next

        return mx