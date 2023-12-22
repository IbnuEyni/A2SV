class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            for j in range(len(image[i])//2):
                image[i][j],image[i][len(image[i])-1-j] = image[i][len(image[i])-1-j], image[i][j]
            for j in range(len(image[0])):
                image[i][j] = 1- image[i][j]
        return image