class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        frq = defaultdict(int)
        mn = len(s)

        for i in range(len(s)):
            frq[s[i]] += 1

        l = 0
        if all(len(s)/4==frq[char] for char in 'QWER'):
            return 0

        for r in range(len(s)):
            frq[s[r]] -= 1

            while l <= r and all(len(s) / 4 >= frq[char] for char in 'QWER'):
                mn = min(mn, r-l+1)
                frq[s[l]] += 1
                l += 1
            
        return mn

        
  
        