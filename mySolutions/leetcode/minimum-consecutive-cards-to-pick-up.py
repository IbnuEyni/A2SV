class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        frq = defaultdict(int)
        mx_ln = float('inf')
        l = 0

        for r in range(len(cards)):
            if cards[r] in frq:
                l = frq[cards[r]]
                mx_ln = min(mx_ln, r-l+1)

            frq[cards[r]] = r
            
        return mx_ln if mx_ln != float('inf') else -1


        