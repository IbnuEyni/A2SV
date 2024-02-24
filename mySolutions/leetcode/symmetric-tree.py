# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(a,b):
            if type(a) == TreeNode and type(b) == TreeNode:
                if a.val == b.val:
                    return sym(a.left, b.right) and sym(a.right, b.left)
            else:
                return a==b
        return sym(root.left, root.right)