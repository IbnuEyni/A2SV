# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, anc, dif):
            anc.append(root.val)
            
            if root.left:
                dif = dfs(root.left, anc, dif)
            if root.right:
                dif = dfs(root.right, anc, dif)
                
            if not root.left and not root.right:
                dif = max(dif, (max(anc)) - (min(anc)))

            anc.pop()
            return dif

        return dfs(root, [], 0)
