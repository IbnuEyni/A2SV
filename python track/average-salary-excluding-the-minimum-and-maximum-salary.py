class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n = float(len(salary) -2)
        min_sal = min(salary)
        max_sal = max(salary)
        
        total = 0
        for i in range(len(salary)):
            if salary[i] != min_sal and salary[i] !=  max_sal:
                total += salary[i]

        return total/n

        