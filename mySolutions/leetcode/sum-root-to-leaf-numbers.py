# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.total = 0
        def sumRL(root, summ):
            
            if not root.left and not root.right:
                self.total += (summ*10 + root.val)
            if root.left:
                sumRL(root.left, summ*10 + root.val)
            if root.right:
                sumRL(root.right, summ*10 + root.val)
            
        sumRL(root, 0)
        return self.total