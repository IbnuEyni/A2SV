class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        for i in range(len(tickets)):
            if i > k:
                if tickets[i] >= tickets[k]:
                    t += tickets[k] - 1
                else:
                    t += tickets[i]
            elif i < k:
                if tickets[i] <= tickets[k]:
                    t += tickets[i]
                else:
                    t += tickets[k]
            elif i == k:
                t += tickets[k]
        return t
