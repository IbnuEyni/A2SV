class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        frq = defaultdict(int)
        mx_no = 0
        l = 0

        for r in range(len(fruits)):
            frq[fruits[r]] += 1

            while len(frq) > 2:
                frq[fruits[l]] -= 1
                if frq[fruits[l]] == 0:
                    del frq[fruits[l]]
                l += 1
            mx_no = max(mx_no, r-l+1)
        return mx_no
            