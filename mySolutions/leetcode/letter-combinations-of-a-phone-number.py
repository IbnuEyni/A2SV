class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapp = {
            '2':'abc', 
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        if not digits:
            return []
        
        def letterComb(idx, string):
            
            if len(string) == len(digits):
                res.append(string)
                return
            for c in mapp[digits[idx]]:
                letterComb(idx + 1, string + c)
                
        letterComb(0, "")
        
        return res
        

