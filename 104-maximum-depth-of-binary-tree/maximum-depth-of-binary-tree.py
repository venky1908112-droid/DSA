# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        q = deque()
        if not root:
            return 0
        q.append((root,1))
        mx = 0
        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
            mx = max(mx, depth)
        return mx