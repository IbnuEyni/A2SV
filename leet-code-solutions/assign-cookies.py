class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse = True)
        s.sort(reverse = True)
        i = j = 0
        cnt = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                i += 1
      
            else:
                cnt += 1
                i += 1
                j += 1

        return cnt
        