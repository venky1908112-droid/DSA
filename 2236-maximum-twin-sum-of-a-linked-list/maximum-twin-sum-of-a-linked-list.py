# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        temp = head
        mx = 0
        for i in range(l):
            if i < (l // 2):
                stack.append(temp.val)
            else:
                mx = max(stack.pop() + temp.val, mx)
            temp = temp.next
        return mx