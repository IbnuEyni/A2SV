
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # MOD = 10**9 + 7

        # def power(a, b):
        #     # if b == 1:
        #     #     return a
        #     if b == 0:
        #         return 1
        #     if a == 0:
        #         return 0
            
        #     res = power(a, b//2) 

        #     res %= (10**9 + 7 )   
        #     res = res * res
        #     res = (a * res) if b % 2 == 1 else res
            

        # even = math.ceil(n/2)
        # odd = n//2
        
        # temp_even = power(5, even)
        # temp_odd = power(4, odd)
        # print(type(temp_odd))
        # print(type(temp_even))

        # return (temp_odd * temp_even) % MOD

        return (pow(5,((n + 1)//2),(10**9 + 7))*pow(4,(n//2),(10**9 + 7)))%1000000007