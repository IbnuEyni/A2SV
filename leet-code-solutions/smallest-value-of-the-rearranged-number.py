class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        ls = sorted(str(abs(num)), reverse = num < 0)
        n_z = next((i for i, n in enumerate(ls) if n!= '0'), 0)
        ls[0], ls[n_z] = ls[n_z], ls[0]
        return int("".join(ls)) * (1 if num >= 0 else -1)
