class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        path = []
        def combSumII(idx, summ):

            if summ == target:           
                res.append(path.copy())
                return 
            if summ > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                combSumII(i+1, summ+candidates[i])
                path.pop()
            
        combSumII(0, 0)
        return res