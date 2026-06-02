"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, depth):
            if not root:
                return depth
            m = 0
            for child in root.children:
                m = max(m, dfs(child, depth + 1))
            return m + 1
        return dfs(root, 0)