class Bitset:

    def __init__(self, size):
        self.bit = [False for i in range(size)]
        self.bitinv = [True for i in range(size)]
        self.size = size
        self.ones = 0
        self.zeros = size
        

    def fix(self, idx):
		
        if not self.bit[idx]:
            self.zeros -= 1
            self.ones += 1
        self.bit[idx] = True
        self.bitinv[idx] = False

    def unfix(self, idx):
		
        if self.bit[idx]:
            self.zeros += 1
            self.ones -= 1
        self.bit[idx] = False
        self.bitinv[idx] = True

    def flip(self):
        self.ones,self.zeros = self.zeros,self.ones
	
        self.bit,self.bitinv = self.bitinv,self.bit

    def all(self):
        return self.ones == self.size

    def one(self):
        return self.ones > 0

    def count(self):
		
        return self.ones

    def toString(self):
		
        ans = ''
        for bit in self.bit:
            if bit:
                ans += '1'
            else:
                ans += '0'
        return ans