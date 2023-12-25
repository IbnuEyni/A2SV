class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum_ = 0
        
        for row in range(len(mat)):
            col = row
            sum_ += mat[row][col]
        
        for row in range(len(mat)):
            col = len(mat) - row -1

            if row == col :
                continue
            sum_ += mat[row][col]
        return sum_

