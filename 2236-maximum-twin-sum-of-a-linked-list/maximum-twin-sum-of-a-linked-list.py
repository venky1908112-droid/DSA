# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        q = deque()
        temp = head
        while temp:
            q.append(temp)
            temp = temp.next
        mx = 0
        while q:
            mx = max(q.popleft().val + q.pop().val, mx)
        return mx