# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def maxValid(root):
            if not root:
                return True, [float('inf'), float('-inf')], 0
            
            l, l_rng, l_sum = maxValid(root.left)
            r, r_rng, r_sum = maxValid(root.right)

 
            if l and r and (l_rng[1] < root.val < r_rng[0]):
                summ = l_sum + r_sum + root.val
                self.ans = max(self.ans, summ)
                return True, [min(l_rng[0], root.val), max(r_rng[1], root.val)], summ
            
            return False, [float('inf'), float('-inf')], None
        
        _, __, ___ = maxValid(root)
        return self.ans
         
