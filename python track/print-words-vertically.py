class Solution:
    def printVertically(self, s):
        yo = s.split()
        max = 0
        for i in yo:
            if len(i)>max: max = len(i)
        m = {}
        for i in yo:
            for j in range(max):
                try:
                    if j not in m:
                        m[j] = i[j]
                    else:
                        m[j]+=i[j]
                except:
                    if j not in m:
                        m[j] = " "
                    else:
                        m[j]+=" "
                    

        res = []
        for i in m:
            res.append(m[i].rstrip())
        return res
       