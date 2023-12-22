class ATM(object):

    def __init__(self):
        self.arr = [0, 0, 0, 0, 0]
        self.d = {0:20, 1:50, 2: 100, 3: 200, 4: 500}        

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(len(banknotesCount)):
            self.arr[i] += banknotesCount[i]
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        l = len(self.arr)
        ans = [0 for i in range(l)]

        k  = l - 1
        while k >= 0 and amount > 0:
            note = self.d[k]
            if amount  >= note and self.arr[k]:
                x = amount // note
                num = min(self.arr[k], x)
                ans[k] = num
                amount -= (note * num)
            k -= 1
        
        if amount == 0:
            for i in range(l):
                self.arr[i] -= ans[i]
            return ans
        else:
            return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)