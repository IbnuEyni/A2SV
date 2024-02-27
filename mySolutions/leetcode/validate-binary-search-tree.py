# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, left, right):
            if not root:
                return True

            if not (left < root.val and root.val < right):
                return False

            bst_left = bst(root.left, left, root.val)
            bst_right = bst(root.right, root.val, right)

            return bst_left and bst_right

        return bst(root, float('-inf'), float('inf'))