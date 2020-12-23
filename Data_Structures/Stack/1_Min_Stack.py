# Link: https://leetcode.com/problems/min-stack/
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if not self.min:
            self.min = x
        else:
            self.min = min(x, self.min)
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
param_3 = obj.top()
param_4 = obj.getMin()
obj.pop()

print(param_3)
print(param_4)
