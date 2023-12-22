class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)-1):
            for col in range(row+1, len(matrix[0])):
                matrix[row][col],matrix[col][row]= matrix[col][row],matrix[row][col]
                # matrix[col][row],matrix[col][len(matrix[0])-1-row] = matrix[col][len(matrix[0])-1-row], matrix[col][row]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])//2):
                matrix[row][col],matrix[row][len(matrix)-1-col] = matrix[row][len(matrix)-1-col],matrix[row][col]