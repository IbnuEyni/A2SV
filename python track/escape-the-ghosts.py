class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        dis_target = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            dis_ghost = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if dis_ghost <= dis_target:
                return False

        return True