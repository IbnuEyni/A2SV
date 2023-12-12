class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.mapp = defaultdict()
        self.timeToLive = timeToLive

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.mapp[tokenId] = currentTime + self.timeToLive
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.mapp:
            timeToExpire = self.mapp[tokenId]
            if timeToExpire > currentTime:
                self.mapp[tokenId] = currentTime + self.timeToLive
        

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        # deletion
        count = 0
        for key, val in self.mapp.items():
            if val <= currentTime:
                pass
            else:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)