# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(root):
            nonlocal s
            if not root:
                return 
            if root.left:
                dfs(root.left)
                if not root.left.left and not root.left.right:
                    s += root.left.val
            if root.right:
                dfs(root.right)
        dfs(root)
        return s        