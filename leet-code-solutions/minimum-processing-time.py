class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        processorTime.sort()
        tasks.sort(reverse=True)
        j = 0
        ls = []
        for i in range(len(processorTime)):
            ls.append(processorTime[i] + tasks[j])
            j += 4
        return max(ls)

        