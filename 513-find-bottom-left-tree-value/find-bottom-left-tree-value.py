# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        ans = 0
        def dfs(root, depth):
            nonlocal ans, max_depth
            if not root:
                return
            if max_depth == depth:
                max_depth += 1
                ans = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return ans