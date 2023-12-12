class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.list = [""]*n
        self.ptr = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.list[idKey-1] = value
        res = []
        if self.ptr == idKey - 1:
            while self.ptr < len(self.list) and self.list[self.ptr] != "":
                print(self.ptr)
                res.append(self.list[self.ptr])
                self.ptr += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)