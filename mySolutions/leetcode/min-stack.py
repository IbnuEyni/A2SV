class Node:
    def __init__(self, val):
        self.val = val
        self.min = None
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        new_node = Node(val)
        new_node.min = self.min
        self.stack.append(new_node)
        self.min = min(self.min, val) 

    def pop(self) -> None:
        new_node = self.stack.pop()
        self.min = new_node.min        

    def top(self) -> int:
        a = self.stack[-1]
        return a.val

    def getMin(self) -> int:
        return self.min        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()