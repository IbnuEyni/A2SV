class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        indices = [0 for i in range(len(s)+1)]
        for i,j,k in shifts:
            if k == 1:
                indices[i] += 1
                indices[j+1] -= 1
            else:
                indices[i] += 25
                indices[j+1] -= 25
        count = 0
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        pos = {alpha[i]:i for i in range(len(alpha))}
        new = ''
        for i in range(len(s)):
            count += indices[i]
            new+=alpha[(count+pos[s[i]])%26]
        return new
        