class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

        self.pre = []
        n = len(self.matrix)
        m = len(self.matrix[0])

        for i in range(n+1):
            self.pre.append([0]*(m+1))
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + self.matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return self.pre[row2+1][col2+1] - self.pre[row2+1][col1] - self.pre[row1][col2+1]  + self.pre[row1][col1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)