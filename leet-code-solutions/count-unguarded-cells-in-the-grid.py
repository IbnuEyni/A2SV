class Solution(object):
    def countUnguarded(self, m, n, guards, walls):


        nums = [[1]*n for i in range(m)]
        for i , j in walls+guards:
            nums[i][j] = 0
            
        direction = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        for di , dj in guards:            
            for x , y in direction:
                i = di
                j = dj
                while 0 <= i+x < m and 0 <= j+y < n and nums[i+x][j+y] != 0:
                    i +=x
                    j +=y
                    nums[i][j] = 3
        count = 0
        for i in range(m):
            for j in range(n):
                if nums[i][j] == 1:
                    count += 1
                    
        return count 
        



































