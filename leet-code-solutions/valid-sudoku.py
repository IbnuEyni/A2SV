class Solution(object):
    def isValidSudoku(self, b):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqr = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if b[r][c] == ".":
                    continue
                if(b[r][c] in cols[c] or b[r][c] in rows[r] or b[r][c] in sqr[(r//3,c//3)]):
                    return False
                cols[c].add(b[r][c])
                rows[r].add(b[r][c])
                sqr[(r//3,c//3)].add(b[r][c])
        return True
