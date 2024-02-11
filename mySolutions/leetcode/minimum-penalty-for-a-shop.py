class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        customers += 'a'
        mapp = customers.count('Y')
        ls = [0] * len(customers)
        N = 0
        Y = 0
        ls[0] = [0, 0]
        for i in range(1, len(customers)):
            
            if customers[i-1] == 'N':
                N += 1
            else:
                Y += 1
            ls[i] = [N, Y]
        
        for j in range(len(customers)):
            ls[j] = ls[j][0] + (mapp - ls[j][1])
        # print(ls)
        temp = min(ls)            
        res = []
        for i, val in enumerate(ls):
            if val == temp:
                res.append(i)      
        return min(res)