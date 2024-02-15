class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        res = 1
        max_=points[0][1]
        print(max_)


        for i in range(1, len(points)):
            if max_ < points[i][0]:
                res+=1
                max_=points[i][1]

        return res
                    