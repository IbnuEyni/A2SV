class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        currentScore = sum(cardPoints[:k])
        maxScore = currentScore
        size = len(cardPoints)
        for i in range(k):
            currentScore += cardPoints[size - 1 - i]
            currentScore -= cardPoints[k - 1 - i]
            maxScore = max(maxScore, currentScore)
            
        return maxScore        