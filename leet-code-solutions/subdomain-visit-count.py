class Solution(object):
    def subdomainVisits(self, cpdomains):
        d = defaultdict(int)
        res = []
        for i in cpdomains:
            curr,domain = i.split()
            curr = int(curr)
            d[domain] += curr
            for i in range(len(domain)):
                if domain[i] == ".":
                    d[domain[i+1:]] += curr
        for i,j in d.items():
            res.append(str(j) +" "+ i)
        return res