# Link https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        # bottom is on the left, top is the right of the array

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            top_value = self.stack[-1]
            self.stack.pop()
            return top_value
        return -1

    def increment(self, k: int, val: int) -> None:
        length = len(self.stack)
        counter = k
        for i in range(0, length):
            # print(self.stack[i])
            self.stack[i] = self.stack[i] + val
            counter -= 1

            if counter == 0:
                break


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
print("Pop value >>>", obj.pop())

obj.push(2)
obj.push(3)
obj.push(4)

print("Stack >>>", obj.stack)

obj.increment(5, 100)
print("Stack >>>", obj.stack)

obj.increment(2, 100)
print("Stack >>>", obj.stack)

print("Pop value >>>", obj.pop())
print("Pop value >>>", obj.pop())
print("Pop value >>>", obj.pop())
print("Pop value >>>", obj.pop())

# param_2 = obj.pop()
obj.increment(3, 10)
# print(param_2)
print(obj.stack)
