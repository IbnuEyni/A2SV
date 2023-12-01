class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
            

        return merged