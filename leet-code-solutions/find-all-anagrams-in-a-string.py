class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map1 = Counter(p)
        k = len(p)
        l = 0
        res = []
        for i in range(k, len(s)+1):
            wind = s[l:i]
            map2 = Counter(wind)

            if map1 == map2:
                res.append(l)
                print(l)
            l += 1
        return res

