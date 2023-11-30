class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if(i-j>=0 and matrix[j][i]!=matrix[0][i-j] or j-i>=0 and matrix[j][i]!=matrix[j-i][0]):
                    return False
        return True