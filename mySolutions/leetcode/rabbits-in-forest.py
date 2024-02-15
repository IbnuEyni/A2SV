class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mapp = defaultdict(int)
        count = Counter(answers)
        print(count)
        cnt = 0

        for i in count:
            print(i)
            if i == 0:
                cnt += count[i]
            elif count[i] <= i + 1:
                cnt += i + 1
            else:
                cnt +=  (ceil(count[i]/(i+1)) * (i + 1))
        return cnt
       