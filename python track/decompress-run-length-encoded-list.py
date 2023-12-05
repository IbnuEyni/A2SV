class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            ans = []
            for j in range(nums[i]):
                ans.append(nums[i+1])
            res.extend(ans)
            # res.extend([nums[i+1] for x in range(nums[i])])
        return res


        #     sub_list = []
        #     sub_list.append(nums[i])
        #     sub_list.append(nums[i+1])
        #     temp = list(str(sub_list[1])*sub_list[0])
        #     res.append(temp)
        # ans = []
        # for k in res:
        #     ans += k
        # final = []
        # for l in ans:
        #     final.append(int(l))
        # return final

        