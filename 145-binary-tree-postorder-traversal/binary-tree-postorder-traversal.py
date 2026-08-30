# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        temp = []
        res = []
        temp.append(root)
        while temp:
            node = temp.pop()
            res.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        res.reverse()
        return res