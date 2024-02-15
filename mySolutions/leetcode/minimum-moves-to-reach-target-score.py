class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt=0
        while maxDoubles > 0 and  target > 1:
            if target%2 == 0 and maxDoubles > 0:
                cnt+=1
                maxDoubles-=1
                target //=2
            else:
                target -=1
                cnt+=1
        if target>1:
            cnt+=target-1
        return cnt 
                