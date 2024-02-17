class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque() 
        for i in s:
            if i in '{([': 
                stack.append(i) 
            else: 
                if not stack:  
                    return False 
                l = stack.pop()
                if l+i != "()" and l+i != "{}" and l+i != "[]":
                    return False 
        return not stack
        # stack = []
        # my_dict  = { "(":")", "{":"}", "[":"]"}

        # for i in s:
        #     if i in my_dict:
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             return False
        #         a = stack.pop()

        #         if i != my_dict[a]:
        #             return False
        # return stack == []