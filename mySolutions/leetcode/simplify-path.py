class Solution:
    def simplifyPath(self, path: str) -> str:
        pth = path.split('/')
        stack = []
        print(pth)

        for i in pth:
            if i == '..':
                if stack:
                    stack.pop()
            if i!= '' and i != '..' and i!='.':
                stack.append(i)
        return "/" + "/".join(stack)
