class UndergroundSystem(object):

    def __init__(self):
        self.mapp_i = defaultdict()
        self.mapp_o = defaultdict(list)
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.mapp_i[id]=(t,stationName)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_time,start_station=self.mapp_i[id]
        total=t-start_time
        self.mapp_o[(start_station,stationName)].append(total)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        res = sum(self.mapp_o[(startStation,endStation)])/len(self.mapp_o[(startStation,endStation)])
        return res

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)