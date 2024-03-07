class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack( o_cnt, c_cnt):
            if c_cnt == o_cnt == n:
                res.append("".join(path))
                return

            if o_cnt < n:
                path.append("(") 
                backtrack(o_cnt+1, c_cnt)
                path.pop()

            if c_cnt < o_cnt:
                path.append(")") 
                backtrack(o_cnt, c_cnt+1)
                path.pop()

        backtrack(0, 0)
        return res