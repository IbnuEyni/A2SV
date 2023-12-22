class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.height = height
        self.width = width
        self.pos = [0,0]
        self.arr = []
        for i in range(width):
            self.arr.append([i, 0])
        for i in range(1, height):
            self.arr.append([width - 1, i])
        for i in range(1, width):
            self.arr.append([width - 1 - i, height - 1])
        for i in range(1, height - 1):
            self.arr.append([0, height - 1 - i])

        self.direction = True
        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        i = self.arr.index(self.pos)

        self.pos = self.arr[(i + num) % (self.width * 2 + self.height * 2 - 4)]

        self.direction = False

        

    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.pos
        

    def getDir(self):
        """
        :rtype: str
        """
        if self.direction:
            return "East"

        if self.pos[0] == 0:
            if self.pos[1] == self.height - 1:
                return "West"
            else:
                return "South"  
				
        if self.pos[0] == self.width - 1:
            if self.pos[1] == 0:
                return "East"
            else:
                return "North"
				
        if self.pos[1] == 0:
            return "East"
        return "West"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()