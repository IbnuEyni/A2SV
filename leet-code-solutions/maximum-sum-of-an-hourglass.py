class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = float('-inf')
        for i in range(len(grid)-2):
            for j in range(1, len(grid[0])-1):
                temp = sum(grid[i][j-1:j+2]) + grid[i+1][j] + sum(grid[i+2][j-1:j+2])
                res = max(res, temp)
        return res