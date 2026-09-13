# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newnode = TreeNode(val)
        if not root:
            return newnode
        def dfs(root):
            if val < root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = newnode
            else:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = newnode

        dfs(root)
        return root