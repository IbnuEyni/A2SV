class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def nice(s):
            sett = set(s)
            if len(s) < 2:
                return ""
            for l in s:
                if ((not l.lower() in sett) or (not l.upper() in sett)):
                    mid = s.index(l)   
                    s1 = nice(s[:mid])
                    s2 = nice(s[mid+1:])
                    return s1 if len(s1)>=len(s2) else s2
            return s
        return nice(s)