# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        stack = [root]

        def dfs(node):
            if not node.left and not node.right:
                ans.append('->'.join([str(x.val) for x in stack]))
                return
            if node.left:
                stack.append(node.left)
                dfs(node.left)
                stack.pop()
            if node.right:
                stack.append(node.right)
                dfs(node.right)
                stack.pop()

        dfs(root)

        return ans

            