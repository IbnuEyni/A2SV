class RandomizedSet(object):

    def __init__(self):
        self.set = []
        self.mapp = defaultdict()


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mapp: return False
        self.mapp[val] = len(self.set)
        self.set.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mapp:
            l = self.set[-1]
            p = self.mapp[val] 

            self.mapp[l] = p
            self.set[p] =  l

            self.mapp.pop(val)
            self.set.pop()

            return True   
        return False


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()