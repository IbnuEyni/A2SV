class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num = list(map(str, nums))
        n = len(num)


        for i in range(n):
            for j in range(n-i-1):
                if num[j] + num[j+1] < num[j+1] + num[j]:
                    num[j], num[j+1] = num[j+1], num[j]
        if num[0] == "0":
            return "0"
        return "".join(num)
        