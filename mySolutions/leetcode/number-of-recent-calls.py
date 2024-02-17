class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        i = 0
        while self.q[i] < t - 3000:
            i += 1
        num_requests = len(self.q) - i
        self.q = self.q[i:]   
        return num_requests



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)