# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, temp, s):
            if not root:
                return 
            temp.append(root.val)
            s += root.val
        
            if s == targetSum and not root.left and not root.right:
                res.append(temp[:])
                
            dfs(root.left, temp, s)
            dfs(root.right, temp, s)

            temp.pop()
        dfs(root, [], 0)
        return res