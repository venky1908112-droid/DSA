# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left_mx, left_mn, right_mx, right_mn):
            if not root:
                return [left_mx, right_mn, True]
            
            valid = False

            mx1, mn1, l_valid = dfs(root.left, left_mx, left_mn, right_mx, right_mn)
            mx2, mn2, r_valid = dfs(root.right, left_mx, left_mn, right_mx, right_mn)

            if l_valid and r_valid and mx1 < root.val < mn2:
                valid = True
            
            return [max(mx1, mx2, root.val), min(mn1, mn2, root.val), valid]

        _, _, ans = dfs(root, float('-inf'), float('inf'), float('-inf'), float('inf'))
        return ans