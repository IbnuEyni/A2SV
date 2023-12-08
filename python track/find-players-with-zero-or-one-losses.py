class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loser = {}
        for i in matches:
            if i[-1] not in loser:
                loser[i[-1]] = 1
            else:
                loser[i[-1]] += 1
        winner = set()
        for i in matches:
            if i[0] not in loser:
                winner.add(i[0])
        los = []
        for i in loser:
            if loser[i] == 1:
                los.append(i)

        win = list(winner)
        win.sort()
        los.sort()

        return [win, los]

