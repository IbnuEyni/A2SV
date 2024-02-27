# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapp = defaultdict(list)
        
        def dfs(root, lvl):
            if not root:
                return None
            mapp[lvl].append(root.val)
            left = dfs(root.left, lvl+1)
            right = dfs(root.right, lvl+1)

        dfs(root, 0)
        res = []
        for i in mapp:
            if i % 2 == 1:
                res.append(reversed(mapp[i]))
            else:
                res.append(mapp[i])
        return res



