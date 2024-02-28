# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mapp = defaultdict(list)

        def inOrder(root, level):
            if not root:
                return None
            
            left = inOrder(root.left, level)
            mapp[level].append(root.val)
            right = inOrder(root.right, level)

        inOrder(root, 0)
       
        return mapp[0][k-1]
