class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        mapp = Counter(s)
        res = 0
        odd = False
        for i in mapp:
            if mapp[i] % 2 == 0:
                res += mapp[i]
            else:
                res += (mapp[i]-1)
                odd = True
        if odd:
            res += 1
            
        return res
            
