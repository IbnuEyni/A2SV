class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        cnt5 = 1
        cnt10 = 0
        for i in range(1, len(bills)):
            
            if bills[i] == 5:
                cnt5 += 1
            elif bills[i] == 10 and cnt5>0:
                cnt10 += 1
                cnt5 -= 1   
            elif bills[i] == 20 and (cnt5>2) or (cnt10>0 and cnt5>0):
                if cnt10 > 0:
                    cnt10 -= 1
                    cnt5 -= 1
                else:
                    cnt5 -= 3
            else:
                return False
            
        return True
           
        # cnt = {5:0, 10:0}
        # for i in bills:
        #     if i == 5 : 
        #         cnt[5] +=1
        #     elif i == 10 and cnt[5]: 
        #         cnt[10] +=1
        #         cnt[5] -= 1
        #     elif i == 20 and ((cnt[5] and cnt[10]) or cnt[5] >=3):
        #         if cnt[5] and cnt[10]:
        #             cnt[5] -= 1
        #             cnt[10] -=1
        #         else: 
        #             cnt[5] -=3
        #     else : return False
        # return True
                