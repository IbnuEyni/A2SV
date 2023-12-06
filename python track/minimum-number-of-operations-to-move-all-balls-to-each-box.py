class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(boxes)):

            temp = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    temp += abs(i-j)
            ans.append(temp)

        return ans