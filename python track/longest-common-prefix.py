class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        length = min(len(s) for s in strs)
        output = ''
        for i in range(length):
            curr_chr = strs[0][i]
            for j in strs:
                if j[i] != curr_chr:
                    return output
            output += curr_chr
            
        return output





























        